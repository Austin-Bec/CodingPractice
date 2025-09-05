# Start with empty list to hold tasks.
tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4:)")

    if choice == "1":
        #TODO loop through tasks and print them.
        print(tasks)
        pass

    elif choice == "2":
        #TODO ask user for a task, then add it to the list
        task = input("Please enter a new task:")
        tasks.append(task)
        pass

    elif choice == "3":
        #TODO ask user which task to remove, then remove it
        remove = input("Please enter a task for removal:")
        tasks.remove(remove)
        pass

    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again.")