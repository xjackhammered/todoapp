def main():
    todos = []
    while True:
        user_input = int(input('''What do you want to do today? 
                            1. Add task 
                            2. View List
                            3. Delete Task
                            4. Exit
                                            '''))
        if user_input == 4:
            exit()
        else:
            choice(user_input, todos)

def choice(user_input, todos):
    if user_input == 1:
        while True:
            task = input("What task do you want to add? (Press 'x' to stop): ").capitalize()
            if task == "X":
                break
            else:
                todos.append(task)
    elif user_input == 2:
        for task in todos:
            print("{}. {}".format((todos.index(task))+1, task))
    elif user_input == 3:
        delete_task = input("Which task do you want to delete? ").capitalize()
        del_index = todos.index(delete_task)
        todos.pop(del_index)
    return todos

main()



        
