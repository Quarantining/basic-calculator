# Basic Calculator
# v1.3

# A simple program that allows a user to select an arithmetic operation to perform on two numbers.
# This is a simple project to help me refresh my basic knowledge on Python code. This project was
# suggested to me by ChatGPT, and I got some help however all the code was written by me.

# functions for arithmetic operations.
def addition(num1, num2):
    result = num1 + num2
    print("Result: " + str(num1) + " + " + str(num2) + " = " + str(result))
def subtraction(num1, num2):
    result = num1 - num2
    print("Result: " + str(num1) + " - " + str(num2) + " = " + str(result))
def multiplication(num1, num2):
    result = num1 * num2
    print("Result: " + str(num1) + " * " + str(num2) + " = " + str(result))
def division(num1, num2):
    result = num1 / num2
    print("Result: " + str(num1) + " / " + str(num2) + " = " + str(result))

# prints the title screen (commands for selecting which operation to use)
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

# while loop so calculator runs indefinitely
running = True
while running:
    # if user enters a valid input:
    try:
        # prompts user to choose a command.
        print("Select arithmetic operation ")
        user_choice = int(input("> "))

        # decision-tree to determine which operation was selected by the user.
        if user_choice == 1: # addition
            print("addition:")
            num1 = int(input("First Number >  "))
            num2 = int(input("Second Number >  "))
            addition(num1, num2)
        elif user_choice == 2: # subtraction
            print("subtraction:")
            num1 = int(input("First Number >  "))
            num2 = int(input("Second Number >  "))
            subtraction(num1, num2)

        elif user_choice == 3: # multiplication
            print("multiplication:")
            num1 = int(input("First Number >  "))
            num2 = int(input("Second Number >  "))
            multiplication(num1, num2)

        elif user_choice == 4: # division
            print("division:")
            num1 = int(input("First Number >  "))
            num2 = int(input("Second Number >  "))
            division(num1, num2)

        elif user_choice == 5: # ends program
            print("Calculator stopped.")
            break

        else: # if an unknown command was entered, program will respond with "Error"
            print('Not a valid input, try again.')

        # prints a blank line after expression result is printed
        print(" ")

    # if user doesn't enters a valid input
    except ValueError:
        print("Not a valid input, try again.")
        print(" ")

    # if user tries to divide by zero
    except ZeroDivisionError:
        print("Cannot divide by Zero.")
        print(" ")
