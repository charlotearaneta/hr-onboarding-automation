from __future__ import annotations
from datetime import datetime, timedelta, date
from pathlib import Path
import json
from typing import Any, Dict


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_date_yyyy_mm_dd(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def due_date_ms(start_date: date, days_after_start: int) -> int:
    d = start_date + timedelta(days=days_after_start)
    # ClickUp expects epoch milliseconds
    return int(datetime(d.year, d.month, d.day).timestamp() * 1000)


def format_template(text: str, ctx: Dict[str, Any]) -> str:
    return text.format(**ctx)

