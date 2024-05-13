# Basic Calculator
# v1.2

# A simple program that allows a user to select an arithmetic operation to perform on two numbers.
# This is a simple project to help me refresh my basic knowledge on Python code. This project was
# suggested to me by ChatGPT.

# arithmetic operations.
def addition(x, y):
    operation = x + y
    print("Result: " + str(operation))
def subtraction(x, y):
    operation = x - y
    print("Result: " + str(operation))
def multiplication(x, y):
    operation = x * y
    print("Result: " + str(operation))
def division(x, y):
    operation = x / y
    print("Result: " + str(operation))

# prints the commands for selecting which operation to use.
print("""
B A S I C  C A L C U L A T O R
- - - - - - - - - - - - - - - -
commands:
1 --> addition
2 --> subtraction
3 --> multiplication
4 --> division
5 --> stop
- - - - - - - - - - - - - - - -
""")

running = True
while running:
    try:
        # prompts user to choose a command.
        print("Select arithmetic operation ")
        user_choice = int(input("> "))

        # elif tree to determine which operation was selected by the user.
        if user_choice == 1:
            print("addition:")
            x = int(input("First Number >  "))
            y = int(input("Second Number >  "))
            addition(x, y)
        elif user_choice == 2:
            print("subtraction:")
            x = int(input("First Number >  "))
            y = int(input("Second Number >  "))
            subtraction(x, y)

        elif user_choice == 3:
            print("multiplication:")
            x = int(input("First Number >  "))
            y = int(input("Second Number >  "))
            multiplication(x, y)

        elif user_choice == 4:
            print("division:")
            x = int(input("First Number >  "))
            y = int(input("Second Number >  "))
            division(x, y)

        elif user_choice == 5:
            print("Program stopped.")
            break

        # if an unknown command was entered, program will respond with "Error"
        else:
            print('Not a valid input, try again.')
        print(" ")
    except (ValueError, ZeroDivisionError):
        print("Not a valid input, try again.")
        print(" ")
