# Basic Calculator
# v1.5
version = "v1.5" # displays the current version on title screen.

# ABOUT PROGRAM:
# A simple program that allows a user to select an arithmetic operation to perform on two numbers.
# This is a simple project to help me refresh my basic knowledge on Python code, and to have a "first" project
# to work on. This project was suggested to me by ChatGPT (however I was already going to do this), and I got some help
# however all the code was written by me! ヽ (◕◡◕) ﾉ

# imports
import math

# functions for arithmetic operations

# traditional
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

# square/sqaure root
def square(num):
    result = num * num
    print("Result: " + str(num) + " ^2 " + " = " + str(result))
def squareroot(num):
    result = math.sqrt(num)
    print("Result: √" + str(num) + " = " + str(result))

# trigonometric functions (the "_1" means it's the inverse) also user inputs must be in radians
def sine(num):
    result = math.sin(num)
    print(f"Result: The sine of {num} is {result}" )
def cosine(num):
    result = math.cos(num)
    print(f"Result: The cosine of {num} is {result}" )
def tangent(num):
    result = math.tan(num)
    print(f"Result: The tangent of {num} is {result}" )
def sine_1(num):
    result = math.asin(num)
    print(f"Result: The sine⁻¹ of {num} is {result}")
def cosine_1(num):
    result = math.acos(num)
    print(f"Result: The cosine⁻¹ of {num} is {result}")
def tangent_1(num):
    result = math.atan(num)
    print(f"Result: The tangent⁻¹ of {num} is {result}")

# prints the title screen (commands for selecting which operation to use)
print(f"""
B A S I C  C A L C U L A T O R
- - - - - - - - - - - - - - - -
commands:

arithmetic operations:
0 --> stop
1 --> addition
2 --> subtraction
3 --> multiplication
4 --> division

square and square root:
5 --> square
6 --> square root  

trigonometric functions (radians):
7 --> sine
8 --> cosine
9 --> tangent
10 --> sine⁻¹
11 --> cosine⁻¹
12 --> tangent⁻¹          {version}
- - - - - - - - - - - - - - - -
""") # "                          {version}"
# comment for amount of spacing to keep version distance consistent (mostly)


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
            num = int(input("Enter Number > "))
            squareroot(num)

        elif user_choice == 7: # sine
            num = int(input("Enter Number > "))
            sine(num)

        elif user_choice == 8: # cosine
            num = int(input("Enter Number > "))
            cosine(num)

        elif user_choice == 9: # tangent
            num = int(input("Enter Number > "))
            tangent(num)

        elif user_choice == 10: # sine⁻¹
            num = int(input("Enter Number > "))
            sine_1(num)

        elif user_choice == 11: # cosine⁻¹
            num = int(input("Enter Number > "))
            cosine_1(num)

        elif user_choice == 12: # tangent⁻¹
            num = int(input("Enter Number > "))
            tangent_1(num)

        elif user_choice == 13:
            print("Nothing here yet")

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
