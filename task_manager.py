tasks = []

while True:
    print("\nTask Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        tasks.append({"description": description, "done": False})
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Done" if task["done"] else "Pending"
                print(f"{i}. {task['description']} [{status}]")

    elif choice == "3":
        task_number = int(input("Enter task number: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
