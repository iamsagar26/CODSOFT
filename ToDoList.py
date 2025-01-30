import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "[✓]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['task']}")

def mark_task_complete(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as complete: "))
            mark_task_complete(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()