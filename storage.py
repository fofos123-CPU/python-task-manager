import json
import os
from typing import List
from models import Task


DATA_DIR = "data"
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")


def load_tasks() -> List[Task]:
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Task.from_dict(item) for item in data]


def save_tasks(tasks: List[Task]) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
