tasks=[]
def add_task(task):
    tasks.append(task)
    print(f"'{task}' added successfully in the TO-Do list")

def remove_task(task):
    if task in tasks:
        tasks.remove()
        print(f"'{task}' removed !!")
    else:
        print("Task not Found")

def list_task():
    if tasks:
        print("To-Do List")
        for i, task in enumerate(tasks,start=1):
            print(f" {i} . {task}")

    else:
        print("Your task is 'EMPTY'")



print("To-Do List")
print("1.Add Task")
print("2.remove task")
print("3.list task")
print("4.Exit")

inp=input("Enter the choice")
if inp=='1':
    task =input("Enter the task to 'add' ")
    add_task(task)
elif inp=='2':
    task =input("Enter the task to 'remove' ")
    remove_task(task)
elif inp=='3':
    list_task()
elif inp=='4':
    print("ThankYou for using the application Byee !!!")
    

else:
    print("Invalid input")
    

