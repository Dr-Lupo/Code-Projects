tasks = []

def addTask():
    task = input ("Please Enter Task: ")
    tasks.append(task)
    print(f"Task'{task}' added to list!")
    
def listTasks():
    if not tasks:
        print("There are no tasks")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks)
            print (f"Task #{index}. {task}")
    
def deleteTask():
        listTasks()
        try:
            taskToDelete = int(input("Choose # of task you want to delete: "))
            if taskToDelete >= 0 and taskToDelete < len(tasks):
                tasks.pop(taskToDelete)
                print(f"Task {taskToDelete} has been deleted")
            else:
                print(f"Task #{taskToDelete} was not found")
                
        except:
            print("Invalid Input") 
            
               




if __name__ == '__main__':
    # Create a loop to run app
    print("Welcome to the to-do list app created by Max Lloyd")
    while True:
        print("\n")
        print("Please Select an option")
        print("-------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        print("-------------------------")
        # Print Menu
        print_menu()
        # Ask for option
        choice = input("Choose an option")
        if (choice == '1'):
            addTask()
        elif (choice =='2'):
            deleteTask()
        elif (choice =='3'):
            listTasks()
        elif (choice =='4'): 
            break
        else:
            print("Invalid, try again.")   
            
    print("Goodbye")        