from __future__ import annotations
import os
import requests
from typing import Any, Dict, Optional, List


class ClickUpClient:
    BASE_URL = "https://api.clickup.com/api/v2"

    def __init__(self, api_token: str):
        self.api_token = api_token
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": self.api_token,
            "Content-Type": "application/json"
        })

    def create_task(
        self,
        list_id: str,
        name: str,
        description: str,
        due_date_ms: Optional[int] = None,
        assignee_id: Optional[str] = None,
        priority: Optional[int] = None,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/list/{list_id}/task"
        payload: Dict[str, Any] = {
            "name": name,
            "description": description
        }

        if due_date_ms is not None:
            payload["due_date"] = due_date_ms

        if assignee_id:
            payload["assignees"] = [assignee_id]

        if priority is not None:
            payload["priority"] = priority

        if tags:
            payload["tags"] = tags

        r = self.session.post(url, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()

