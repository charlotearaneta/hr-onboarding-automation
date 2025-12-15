from __future__ import annotations
from typing import Dict, Any


ASSIGNEE_MAP_DEFAULT = {
    "hr": None,       # fallback to DEFAULT_ASSIGNEE_ID if set
    "it": None,
    "manager": None
}


def resolve_assignee_id(task_assignee_key: str, default_assignee_id: str | None) -> str | None:
    """
    If you later know real ClickUp user IDs for HR/IT/Manager, replace the map values.
    For MVP we fall back to DEFAULT_ASSIGNEE_ID (optional).
    """
    if default_assignee_id:
        return default_assignee_id
    return None

