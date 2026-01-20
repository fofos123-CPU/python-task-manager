from typing import List
from models import Task
from storage import load_tasks, save_tasks


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = load_tasks()

    def _get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title: str) -> Task:
        task = Task(id=self._get_next_id(), title=title)
        self.tasks.append(task)
        save_tasks(self.tasks)
        return task

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                save_tasks(self.tasks)
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                save_tasks(self.tasks)
                return True
        return False
