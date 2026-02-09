# Simple To-Do List Application
# Developed as Task 1 for CodSoft Python Internship
# This program allows users to manage daily tasks

todo_list = []

def show_menu():
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your favorite choice (1-5): ")

    # ADD TASK
    if choice == "1":
        task_title = input("Enter task name: ")
        task_data = {
            "task": task_title,
            "status": "Processing"
        }
        todo_list.append(task_data)
        print("Task added successfully")

    # VIEW TASKS
    elif choice == "2":
        if not todo_list:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(todo_list, start=1):
                print(f"{i}. {t['task']} - {t['status']}")

    # UPDATE TASK
    elif choice == "3":
        if not todo_list:
            print("No tasks to update")
        else:
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(todo_list):
                todo_list[task_no - 1]["status"] = "Completed"
                print("Task marked as completed")
            else:
                print("Invalid task number")

    # DELETE TASK
    elif choice == "4":
        if not todo_list:
            print("No tasks to delete")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(todo_list):
                removed = todo_list.pop(task_no - 1)
                print(f"Task '{removed['task']}' deleted")
            else:
                print("Invalid task number")

    # EXIT
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Please enter a valid option (1-5)")
