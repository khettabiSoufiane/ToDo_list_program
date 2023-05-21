# ToDo list program
todo_list = []

# application the logic of program todo list
while(True):
    item = input("you want to (add, view, remove or exit): ").lower()

    if item == "add":
        todo_list.append(input("enter your task: ").lower())
        print("task added")
    elif item == "view":
        if not todo_list:
            print("There are not tasks")
        else:
            for task in todo_list:
                print(task)
    elif item == "remove":
        if not todo_list:
            print("There are not tasks")
        else:
            for task in todo_list:
                task_remove = input("entre your task to remove: ").lower()
                if task == task_remove:
                    todo_list.remove(task_remove)
                    print("task removed")
                else:
                    print("Task not found,entre your task to remove.")
    elif item == "exit":
        print("program exit")
        break
    else:
        print("invalid option, enter(add, view, remove or exit).")

