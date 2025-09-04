def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b

while True: 
    a = int(input("Please enter the first number: "))

    b = int(input("Please enter the second number: "))

    choice = input("Please choose a operation(+, -, *, /):")

    if choice == "q":
        print("Goodbye!")
        break   

    elif choice == "+":
        print("Result::", add(a, b))

    elif choice == "-":
        print("Result:", subtract(a, b))

    elif choice == "*":
        print("Result:", multiply(a, b))

    elif choice == "/":
        if b != 0:
            print("Result:", divide(a, b))
        else:
            print("Error, cannot divide by zero!")
    
    else:
        print("Invalid choice.")