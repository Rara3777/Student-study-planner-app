ffrom tasks import add_task, view_tasks, mark_done, load_tasks, save_tasks, prioritize_tasks ,delete_task

def menu():
    tasks = load_tasks()

    while True:
        print("\n--- Study Planner ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Change Priority")
        print("6. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            prioritize_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


menu()
