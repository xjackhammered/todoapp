def main():
    task_list = []
    
    while True:
        print('''Choose an option
                    1. Add Task
                    2. Delete Task
                    3. View Tasks
                    4. Clear todo list
                    5. Exit
                    ''')
        n = int(input("Choose an option: "))
        if n == 1:
            add_task(task_list)
        elif n == 2:
            delete_task()
        elif n == 3:
            view_tasks()
        elif n == 4:
            clear_list()
        elif n == 5:
            exit()
        
def add_task(task_list):
    while True:
        print("Input tasks or press 'x' to exit: ")
        task = input("Input task: ")
        if task.upper() == "X":
            break
        else:
            task_list.append(task)
        with open("todos.txt","w") as file:
            for tasks in task_list:
                file.write(tasks + "\n")


def delete_task():

    del_task = input("Type the name of the task that you want to delete: ").strip().capitalize()

    with open("todos.txt", "r") as file:
        content = file.readlines()

    found = False
    for i in range(len(content)):
        task = content[i].strip()

        if task.capitalize() == del_task:
            found = True
            del content[i]
            print("Deleted Successfully!")
            break

    if not found:
        print("Task not found!")
        return

    with open("todos.txt", "w") as file:
        for task in content:
            file.write(task)

def clear_list():
    with open("todos.txt","r") as file:
        content = file.readlines()

    with open("todos.txt","w") as file:
        content.clear()
        for i in content:
            file.write(i)
    
    print("List is cleared successfully!")

def view_tasks():
    with open("todos.txt","r") as file:
        read_content = file.readlines()
        for i in read_content:
            print("{}.{}".format(read_content.index(i)+1,i.rstrip().capitalize()))


main()
