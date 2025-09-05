students = {"Austin": 90}   # dictionary: { "Name": grade }


def view_students():
    # loop through dictionary and print students
    for name, grade in students.items():
        print(f"{name}: {grade}")
    pass

def add_student():
    # ask for name & grade, add to dictionary
    name = input("Please enter student Name: ")
    grade = int(input("Please enter student Grade: "))
    
    students[name] = grade
    print(f"Added {name} with grade {grade}")
    

def update_grade():
    # ask for student name, update grade
    name = input("Enter the name of the student that you want update:")

    if name in students:
        new_grade = int(input(f"Enter the new grade for {name}: "))
        students[name] = new_grade
        print(f"{name}'s grade has been updated.")
    else:
        print(f"{name} was not found in the grade book.")
    

def remove_student():
    # ask for student name, remove from dictionary
    name = input("Please enter the name of the student you wish to remove: ")
    
    if name in students:
        del students[name]
        print(f"Removed {name} from grade book.")
    else:
        print(f"{name} was not found in grade book.")
    

def class_average():
    # calculate and print average of all grades
    if len(students) == 0:
        print("No students in the grade book.")
    else:
        avg = sum(students.values()) / len(students)
        print(f"Class average: {avg:.2f}")
    

while True:
    print("\n--- Student Gradebook Menu ---")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Grade")
    print("4. Remove Student")
    print("5. Class Average")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_grade()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        class_average()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
