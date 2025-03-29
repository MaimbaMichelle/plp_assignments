# Basic Calculator Program

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Input: Ask the user for two numbers and the operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == "-":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == "*":
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == "/":
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid operation! Please enter one of +, -, *, /.")
