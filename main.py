from task_manager import TaskManager


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nTasks:")
    for task in tasks:
        status = "✓" if task.completed else " "  # M
        print(f"[{status}] {task.id}. {task.title}")
    print()


def main():
    manager = TaskManager()

    while True:
        print("=== Task Manager ===")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            show_tasks(manager.list_tasks())

        elif choice == "2":
            title = input("Task title: ")
            manager.add_task(title)
            print("Task added.\n")

        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            if manager.complete_task(task_id):
                print("Task completed.\n")
            else:
                print("Task not found.\n")

        elif choice == "4":
            task_id = int(input("Task ID to delete: "))
            if manager.delete_task(task_id):
                print("Task deleted.\n")
            else:
                print("Task not found.\n")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
