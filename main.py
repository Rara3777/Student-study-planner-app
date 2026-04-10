from tasks import add_task, view_tasks, mark_done, load_tasks, save_tasks, prioritize_tasks, delete_tasks

tasks = load_tasks()  # Load tasks from data.txt

while True:
    print("\n--- Student Study Planner ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Priortize your task")
    print("5. Delete tasks")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        prioritize_tasks(tasks)
    elif choice == "5":
        delete_task(tasks)
    elif choice == "6":
        save_tasks(tasks)
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
