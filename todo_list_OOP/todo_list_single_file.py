class TodoList:
    """
    This class represents a todo list, which allows users to add, view, and remove tasks.

    Attributes:
        todo_list (list): A list to store the tasks.

    Methods:
        __init__(): Initializes an empty todo list.
        add(): Prompts the user to enter a task and adds it to the todo list.
        view(): Displays all the tasks in the todo list.
        remove(): Prompts the user to enter a task to remove and removes it from the todo list.
    """

    def __init__(self):
        """
        Initializes an empty todo list.
        """
        self.todo_list = []

    def add(self):
        """
        Prompts the user to enter a task and adds it to the todo list.
        """
        task = input("Enter your task: ").lower()
        self.todo_list.append(task)
        print("Task added.")

    def view(self):
        """
        Displays all the tasks in the todo list.
        """
        if not self.todo_list:
            print("There are no tasks.")
        else:
            print("Todo List:")
            for task in self.todo_list:
                print(task)

    def remove(self):
        """
        Prompts the user to enter a task to remove and removes it from the todo list.
        """
        if not self.todo_list:
            print("There are no tasks.")
        else:
            task_remove = input("Enter the task to remove: ").lower()
            if task_remove in self.todo_list:
                self.todo_list.remove(task_remove)
                print("Task removed.")
            else:
                print("Task not found.")


class TodoListManager:
    """
    This class manages the interaction with the TodoList class and provides a command-line interface for the user.

    Attributes:
        todo_list (TodoList): An instance of the TodoList class.

    Methods:
        __init__(): Initializes the TodoListManager with a TodoList instance.
        run(): Runs the main loop to process user commands and interact with the TodoList.
    """

    def __init__(self):
        """
        Initializes the TodoListManager with a TodoList instance.
        """
        self.todo_list = TodoList()

    def run(self):
        """
        Runs the main loop to process user commands and interact with the TodoList.
        """
        while True:
            item = input("What do you want to do (add, view, remove, or exit)? ").lower()

            if item == "add":
                self.todo_list.add()
            elif item == "view":
                self.todo_list.view()
            elif item == "remove":
                self.todo_list.remove()
            elif item == "exit":
                print("Program exit.")
                break
            else:
                print("Invalid option. Please enter (add, view, remove, or exit).")


if __name__ == "__main__":
    manager = TodoListManager()
    manager.run()
