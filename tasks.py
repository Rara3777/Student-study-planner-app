def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Enter priority (High / Medium / Low): ").lower()

    if priority not in ["high", "medium", "low"]:
        priority = ""

    tasks.append({
        "task": task,
        "done": False,
        "priority": priority
    })

    print("Task added!")


def get_sorted_tasks(tasks):
    priority_order = {"high": 1, "medium": 2, "low": 3}

    return sorted(
        tasks,
        key=lambda t: priority_order.get(t.get("priority", "").lower(), 4)
    )


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return []

    sorted_tasks = get_sorted_tasks(tasks)

    print("\n--- Your Tasks (Sorted by Priority) ---")
    for i, t in enumerate(sorted_tasks):
        status = "✅" if t["done"] else "❌"
        priority = t.get("priority", "None")
        print(f"{i+1}. {t['task']} [{status}] (Priority: {priority})")

    return sorted_tasks


def mark_done(tasks):
    sorted_tasks = view_tasks(tasks)
    if not sorted_tasks:
        return

    try:
        index = int(input("Enter task number to mark done: ")) - 1

        if 0 <= index < len(sorted_tasks):
            sorted_tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")


def delete_task(tasks):
    sorted_tasks = view_tasks(tasks)
    if not sorted_tasks:
        return

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(sorted_tasks):
            tasks.remove(sorted_tasks[index])
            print("Task deleted!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")


def prioritize_tasks(tasks):
    sorted_tasks = view_tasks(tasks)
    if not sorted_tasks:
        return

    try:
        index = int(input("Enter task number to prioritize: ")) - 1

        if 0 <= index < len(sorted_tasks):
            new_priority = input("Enter priority (High / Medium / Low): ").lower()

            if new_priority in ["high", "medium", "low"]:
                sorted_tasks[index]["priority"] = new_priority
                print("Priority updated!")
            else:
                print("Invalid priority.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Enter a valid number.")


# ---------------- FILE HANDLING ----------------

def load_tasks():
    tasks = []

    try:
        with open("data.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")

                if len(parts) == 3:
                    task, done, priority = parts
                elif len(parts) == 2:
                    task, done = parts
                    priority = ""
                else:
                    continue

                tasks.append({
                    "task": task,
                    "done": done == "True",
                    "priority": priority
                })

    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    with open("data.txt", "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['done']}|{t.get('priority','')}\n")
