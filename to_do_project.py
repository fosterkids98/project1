tasks = []
option_check = True
import time


print("Welcome to Your To Do List what would you like to do?")


while option_check:    
    choice = input("Add Task    View Tasks    Delete Task    Quit\nEnter you selction.\n")

    if choice.title().strip() == "View Tasks":        
        for task in tasks:
            print(f"-{task}")

        time.sleep(2)

        

    if choice.title().strip() == 'Add Task':        
        try:
            add_task = input("What would your like you task to be?\n")

            tasks.append(add_task.lower())

        except NameError: 
            print("Try again later.")

            time.sleep(2)

    if choice.title().strip() == 'Delete Task':
        try:
            for task in tasks:
                print(f'-{task}')

            remove_task = input('Which task would you like to delete?\n').lower()
            
            if remove_task in tasks:
                tasks.remove(remove_task) 
                
                print("Deleting Task")

                time.sleep(1)

                print("Task Deleted")

                time.sleep(1)
            
            else:                
                print("Task not listed")

                time.sleep(1.5)
        
        except NameError:
            print("Try again later.")
            
            time.sleep(2)

    if choice.title().strip() == 'Quit':
        option_check = False

    if choice.title().strip() != 'Add Task' and choice.title(
    ).strip() != 'View Tasks' and choice.title().strip() != 'Delete Task' and choice.title(
    ).strip() != 'Quit':
        print("Please try again.")
        
        time.sleep(2)
        

    