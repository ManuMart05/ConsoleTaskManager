# Simple Task Manager
# This program allows the user to add tasks, view them,
# mark tasks as completed, and exit the program.

# List to store all tasks

import json

FILE_NAME = "tasks.json"
tasks = []


def load_tasks():
    """Load tasks from a JSON file if it exists and is valid."""
    global tasks
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []


def save_tasks():
    """Save tasks to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_menu():
    """Display the main menu."""
    print("\nTask Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    """Add a new task."""
    description = input("Enter task description: ")
    tasks.append({"description": description, "done": False})
    save_tasks()
    print("Task added.")


def view_tasks():
    """View all tasks."""
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['description']} [{status}]")


def complete_task():
    """Mark a task as completed."""
    try:
        task_number = int(input("Enter task number: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Delete a task by number."""
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            save_tasks()
            print(f"Deleted task: {removed['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
