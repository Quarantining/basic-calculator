# Basic Calculator
# v1.4
version = "v1.4" # displays the current version on title screen.

# ABOUT PROGRAM:
# A simple program that allows a user to select an arithmetic operation to perform on two numbers.
# This is a simple project to help me refresh my basic knowledge on Python code, and to have a "first" project
# to work on. This project was suggested to me by ChatGPT (however I was already going to do this), and I got some help
# however all the code was written by me! ヽ (◕◡◕) ﾉ

# imports
import math

# functions for arithmetic operations
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
def square(num):
    result = num * num
    print("Result: " + str(num) + " ^2 " + " = " + str(result))
def squareroot(num):
    result = math.sqrt(num)
    print("Result: √" + str(num) + " = " + str(result))

# prints the title screen (commands for selecting which operation to use)
print(f"""
B A S I C  C A L C U L A T O R
- - - - - - - - - - - - - - - -
commands:
0 --> stop
1 --> addition
2 --> subtraction
3 --> multiplication
4 --> division
5 --> square
6 --> square root         {version}
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

        elif user_choice == 5: # squaring
            num = int(input("Enter Number >  "))
            square(num)

        elif user_choice == 6: # square root
            num = int(input("Enter aNumber > "))
            squareroot(num)

        elif user_choice == 0: # ends program
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
