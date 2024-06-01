# Simple Task Manager

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Remove Task")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')

def complete_task(tasks):
    task_number = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print(f'Task "{tasks[task_number]["task"]}" marked as completed.')
    else:
        print("Invalid task number.")

def remove_task(tasks):
    task_number = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f'Task "{removed_task["task"]}" removed.')
    else:
        print("Invalid task number.")

    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{i + 1}. {task['task']} - {status}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            complete_task(tasks)
        elif choice == "3":
            remove_task(tasks)
            
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
