import json
import argparse
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_name):
    tasks = load_tasks()
    task_id = len(tasks) + 1

    task = {
        "id": task_id,
        "task": task_name,
        "status": "todo"
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task_name}")

def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [t for t in tasks if t["status"] == status]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f'{task["id"]}. [{task["status"]}] {task["task"]}')

# Update task
def update_task(task_id, new_status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print("Task updated.")
            return

    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]

    save_tasks(tasks)
    print("Task deleted.")

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("task")

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--status", choices=["todo", "in-progress", "done"])

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int)
    update_parser.add_argument("status", choices=["todo", "in-progress", "done"])

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.task)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "update":
        update_task(args.id, args.status)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()