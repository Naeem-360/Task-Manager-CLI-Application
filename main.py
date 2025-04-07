from task import load_tasks, save_tasks, add_tasks, mark_done, delete_tasks

FILENAME = "data.txt"

def show_menu():
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark as Done")
    print("4. Delete Task")
    print("5. Exit")

def show_task(tasks):
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    
    if not tasks:
        print("No task to view")

def exit_app(tasks):
    save_tasks(tasks, FILENAME)
    exit()

def main():
    tasks = load_tasks(FILENAME)

    while True:
        show_menu()
        user_choice = int(input("Choose an option (1-5): "))

        choices = {
            1:lambda:show_task(tasks),
            2:lambda:add_tasks(input("Enter new task: "), tasks),
            3:lambda:mark_done(int(input("Task number to mark done: ")) - 1, tasks),
            4:lambda:delete_tasks(int(input("Task number to delete: ")) - 1, tasks),
            5:lambda:exit_app(tasks)

        }
        
        choice = choices.get(user_choice)

        if choices:
            choice()
        else:
            print("Invalid choice!")
    

if __name__ == "__main__":
   main()

