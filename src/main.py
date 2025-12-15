from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv

from clickup_client import ClickUpClient
from templates import resolve_assignee_id
from utils import load_json, parse_date_yyyy_mm_dd, due_date_ms, format_template

load_dotenv()

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"

CHECKLIST_PATH = DATA_DIR / "onboarding_checklist.json"


def build_context(new_hire: Dict[str, Any]) -> Dict[str, Any]:
    # Required fields expected in new_hire.json
    required = ["full_name", "email", "role", "start_date", "manager_name", "department"]
    missing = [k for k in required if k not in new_hire or not str(new_hire[k]).strip()]
    if missing:
        raise ValueError(f"Missing required fields in new_hire.json: {missing}")

    ctx = dict(new_hire)
    # normalize
    ctx["start_date_obj"] = parse_date_yyyy_mm_dd(ctx["start_date"])
    return ctx


def run_mvp(new_hire_path: Path) -> Dict[str, Any]:
    api_token = os.getenv("CLICKUP_API_TOKEN")
    list_id = os.getenv("CLICKUP_LIST_ID")
    default_assignee_id = os.getenv("DEFAULT_ASSIGNEE_ID") or None
    default_priority = os.getenv("DEFAULT_PRIORITY")

    if not api_token:
        raise RuntimeError("Missing CLICKUP_API_TOKEN in .env")
    if not list_id:
        raise RuntimeError("Missing CLICKUP_LIST_ID in .env")

    priority = int(default_priority) if (default_priority and default_priority.isdigit()) else None

    new_hire = load_json(new_hire_path)
    ctx = build_context(new_hire)

    checklist = load_json(CHECKLIST_PATH)
    tags = checklist.get("default_tags", [])

    client = ClickUpClient(api_token=api_token)

    created_tasks: List[Dict[str, Any]] = []

    for t in checklist["tasks"]:
        title = format_template(t["title"], ctx)
        description = format_template(t["description"], ctx)
        days = int(t.get("days_after_start", 0))
        due_ms = due_date_ms(ctx["start_date_obj"], days)

        assignee_key = t.get("assignee", "hr")
        assignee_id = resolve_assignee_id(assignee_key, default_assignee_id)

        task = client.create_task(
            list_id=list_id,
            name=title,
            description=description,
            due_date_ms=due_ms,
            assignee_id=assignee_id,
            priority=priority,
            tags=tags
        )

        created_tasks.append({
            "id": task.get("id"),
            "url": task.get("url"),
            "name": task.get("name"),
            "due_date": task.get("due_date")
        })

        print(f"✅ Created: {task.get('name')}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output = {
        "new_hire": {
            "full_name": ctx["full_name"],
            "email": ctx["email"],
            "role": ctx["role"],
            "start_date": ctx["start_date"],
            "manager_name": ctx["manager_name"],
            "department": ctx["department"]
        },
        "clickup_list_id": list_id,
        "tasks_created": created_tasks
    }

    out_path = RESULTS_DIR / f"onboarding_run_{ctx['full_name'].replace(' ', '_').lower()}.json"
    out_path.write_text(__import__("json").dumps(output, indent=2), encoding="utf-8")
    print(f"\n📦 Saved run log: {out_path}")

    return output


def main():
    parser = argparse.ArgumentParser(description="Employee Onboarding Automation (MVP)")
    parser.add_argument("--new-hire", required=True, help="Path to new hire JSON (e.g., data/new_hire.json)")
    args = parser.parse_args()

    new_hire_path = Path(args.new_hire)
    if not new_hire_path.exists():
        raise FileNotFoundError(f"New hire file not found: {new_hire_path}")

    run_mvp(new_hire_path)


if __name__ == "__main__":
    main()

