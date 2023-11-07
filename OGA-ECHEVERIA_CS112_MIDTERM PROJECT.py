# Welcome to the Para sa gwapo Calculator
# This program performs basic arithmetic operations.

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exponent' for exponentiation")
    print("Enter 'quit' to end the program")

    # Get user's choice of operation
    user_input = input(": ")

    if user_input == "quit":
        print("Thank you for using the Para sa gwapo  Calculator. mwa!")
        break
    elif user_input in ["add", "subtract", "multiply", "divide", "exponent"]:
        # Get the user's numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            # Perform addition
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif user_input == "subtract":
            # Perform subtraction
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif user_input == "multiply":
            # Perform multiplication
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif user_input == "divide":
            if num2 == 0:
                # Check for division by zero
                print("Error: Division by zero is not allowed.")
            else:
                # Perform division
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        elif user_input == "exponent":
            # Perform exponentiation
            result = num1 ** num2
            print(f"Result: {num1} ^ {num2} = {result}")
    else:
        # Handle invalid input
        print("Invalid input. Please enter a valid option.")

# End of the program
