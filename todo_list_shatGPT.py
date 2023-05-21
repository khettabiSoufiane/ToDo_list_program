def add(todo_list):
    """
    Adds a task to the todo list.

    Parameters:
    - todo_list (list): The list to which the task will be added.

    Returns:
    - None
    """

    task = input("Enter your task: ").lower()
    todo_list.append(task)
    print("Task added.")

def view(todo_list):
    """
    Displays all tasks in the todo list.

    Parameters:
    - todo_list (list): The list containing the tasks.

    Returns:
    - None
    """

    if not todo_list:
        print("There are no tasks.")
    else:
        print("Todo List:")
        for task in todo_list:
            print(task)

def remove(todo_list):
    """
    Removes a task from the todo list.

    Parameters:
    - todo_list (list): The list from which the task will be removed.

    Returns:
    - None
    """

    if not todo_list:
        print("There are no tasks.")
    else:
        task_remove = input("Enter the task to remove: ").lower()
        if task_remove in todo_list:
            todo_list.remove(task_remove)
            print("Task removed.")
        else:
            print("Task not found.")

def main():
    """
    Main function to run the todo list program.

    Parameters:
    - None

    Returns:
    - None
    """

    todo_list = []

    while True:
        item = input("What do you want to do (add, view, remove, or exit)? ").lower()

        if item == "add":
            add(todo_list)
        elif item == "view":
            view(todo_list)
        elif item == "remove":
            remove(todo_list)
        elif item == "exit":
            print("Program exit.")
            break
        else:
            print("Invalid option. Please enter (add, view, remove, or exit).")

if __name__ == "__main__":
    main()
