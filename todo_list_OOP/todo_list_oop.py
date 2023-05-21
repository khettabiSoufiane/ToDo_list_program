class TodoList:
    def __init__(self) -> None:
        self.todo_list = []

    def add(self):
       self.todo_list.append(input("Enter your task: ").lower())
       print("task added")

    def view(self):
        if not self.todo_list:
            print("There are not tasks")
        else:
            for task in self.todo_list:
                print(task)        

    def remove(self):
        if not self.todo_list:
            print("There are not tasks")
        else:
            for task in self.todo_list:
                task_remove = input("entre your task to remove: ").lower()
                if task == task_remove:
                    self.todo_list.remove(task_remove)
                    print("task removed")   
   