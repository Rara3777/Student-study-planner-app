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
def prioritize_tasks(tasks):
    for i, tasks in enumerate(tasks):
        print(f"{i+1}.{task["name"]}. (Priority: {task['priority']})")
    choice = int(input("Enter the number of the task to priortize: "))

if 0 <= choice <len(tasks):
    new_priority = input("Enter the importance of your task to priortize: [ High,Medium,Low ]: ").lower()
    if new_priority in ["High", "Medium", "Low"]:
            tasks[choice]['priority'] = new_priority
            print(f"Priority updated to {new_priority}!")
        else:
            print("Invalid priority. Try again.")
    else:
        print("Invalid task number.")
