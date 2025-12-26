# Simple Task Manager
# Refactored version using functions

tasks = []


def show_menu():
    """Displays the main menu options."""
    print("\nTask Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")


def add_task():
    """Adds a new task to the task list."""
    description = input("Enter task description: ")
    tasks.append({"description": description, "done": False})
    print("Task added.")


def view_tasks():
    """Displays all tasks with their status."""
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['description']} [{status}]")


def complete_task():
    """Marks a selected task as completed."""
    try:
        task_number = int(input("Enter task number: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main program loop."""
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
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


# Program entry point
main()

