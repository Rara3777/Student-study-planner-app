def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}. {t['task']} [{status}]")

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def load_tasks():
    tasks = []
    try:
        with open("data.txt", "r") as file:
            for line in file:
                task, done = line.strip().split("|")
                tasks.append({"task": task, "done": done == "True"})
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open("data.txt", "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['done']}\n")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task successfully deleted !")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")
def prioritize_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to change priority: ")) - 1

        if 0 <= index < len(tasks):
            new_priority = input("Enter new priority (High:1 / Medium:2 / Low:3): ")
            if new_priority == "1":
                tasks[index]["priority"] = new_priority
                print("Task priority updated as important task!")
            elif new_priority == "2":
                tasks[index]["priority"] = new_priority
                print("Task priority updated as average task!")
            elif new_priority == "1":
                tasks[index]["priority"] = new_priority
                print("Task priority updated as not that imposrtant task!")
            else:
                print("Task didn't priortize because of invalid response")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")
