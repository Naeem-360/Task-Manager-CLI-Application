def load_tasks(filename):
    while True:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

def save_tasks(tasks,filename):
    with open(filename, "w") as write_file:
        for task in tasks:
            write_file.write(task + "\n")

def add_tasks(task, tasks):
    tasks.append("[ ]" + task)

def mark_done(index, tasks):
    if 0 <= index < len(tasks):
        tasks[index] = tasks[index].replace("[ ] ", "[X]")

def delete_tasks(index, tasks):
    if 0 <= index < len(tasks):
        tasks.pop(index)



