# Simple Task Manager
# This program allows the user to add tasks, view them,
# mark tasks as completed, and exit the program.

# List to store all tasks
tasks = []

# Main program loop (runs until the user chooses to exit)
while True:
    # Display menu options
    print("\nTask Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

   # Get user choice
    choice = input("Choose an option: ")

    # Option 1: Add a new task
    if choice == "1":
        description = input("Enter task description: ")
        # Each task is stored as a dictionary
        tasks.append({"description": description, "done": False})
        print("Task added.")

    # Option 2: View all tasks
    elif choice == "2":
         # Check if there are any tasks
        if not tasks:
            print("No tasks yet.")
        else:
            # Loop through tasks and display them
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Pending"
                print(f"{i}. {task['description']} [{status}]")

    # Option 3: Mark a task as completed
    elif choice == "3":
        # Ask the user which task to complete
        task_number = int(input("Enter task number: "))

        # Validate task number
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    # Option 4: Exit the program
    elif choice == "4":
        print("Goodbye!")
        break

    # Handle invalid menu options
    else:
        print("Invalid option.")

