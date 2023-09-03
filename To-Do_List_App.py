# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to remove a task by index
def remove_task(index):
    if 1 <= index <= len(tasks):
        task = tasks.pop(index - 1)
        print(f"Task '{task}' removed.")
    else:
        print("Invalid task index.")

# Main loop for the to-do list app
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")