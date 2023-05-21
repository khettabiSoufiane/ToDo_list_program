from todo_list_oop import TodoList

class TodoList_manager:
    def __init__(self) -> None:
        self.todo_list = TodoList()

    def run(self):

        while True:

            item = input("you want to (add, view, remove or exit): ").lower()

            if item == "add":
                self.todo_list.add()
            elif item == "view":
                self.todo_list.view()
            elif item == "remove":
                self.todo_list.remove()
            elif item == "exit":
                print("program exit")
                break
            else:
                print("invalid option, enter(add, view, remove or exit).")                           