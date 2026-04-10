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
def prioritize_tasks(tasks):
    view_tasks(tasks)
    while True:
        
        index_t = int(input("Enter the number of the task to priortize: ")) - 1
    
        if 0 <= index_t <len(tasks):
            new_priority = input("Enter the importance of your task to priortize: [ High,Medium,Low ]: ").lower()
            if new_priority.lower() in ["high", "medium", "low"]:
                
                tasks[index_t]['priority'] = new_priority
                print(f"Priority updated to {new_priority}!")
                break
            else:
                print("Invalid priority. Try again.")
        else:
            print("Invalid task number.")
             
    print(f"These are your tasks  with priority")
    for i, task in enumerate(tasks):
        print(f"{i+1}.{task['task']}. Priority: {task.get('priority', 'DefaultValue')}")
