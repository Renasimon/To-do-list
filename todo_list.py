todo_list = []

def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f'"{task}" has been added.')

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            removed = todo_list.pop(task_num - 1)
            print(f'"{removed}" has been removed.')
        except (ValueError, IndexError):
            print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option.")
