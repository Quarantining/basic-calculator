# Basic Calculator
# v1.0

# A simple program that allows a user to select an arithmetic operation to perform on two numbers.
# This is a simple project to help me refresh my basic knowledge on Python code. This project was
# suggested to me by ChatGPT.

# arithmetic operations.
def addition(x, y):
    operation = x + y
    print(operation)
def subtraction(x, y):
    operation = x - y
    print(operation)
def multiplication(x, y):
    operation = x * y
    print(operation)
def division(x, y):
    operation = x / y
    print(operation)

# prints the commands for selecting which operation to use.
print("""
commands:
1 --> addition
2 --> subtraction
3 --> multiplication
4 --> division
""")

# elif tree to determine which operation was selected by the user.
if user_choice == 1:
    x = int(input(">"))
    y = int(input(">"))
    addition(x, y)
elif user_choice == 2:
    x = int(input(">"))
    y = int(input(">"))
    subtraction(x, y)

elif user_choice == 3:
    x = int(input(">"))
    y = int(input(">"))
    multiplication(x, y)

elif user_choice == 4:
    x = int(input(">"))
    y = int(input(">"))
    division(x, y)

# if an unknown command was entered, program will respond with "Error"
else:
    print('Error')
