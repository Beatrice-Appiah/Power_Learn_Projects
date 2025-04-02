# Simple calculator program

# Prompting the user to input two numbers of choice
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompting the user to input a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Performing the chosen operation and displaying the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
