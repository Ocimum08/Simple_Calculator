def simple_calculator():
    print("Welcome to the Simple Calculator!")
    
    # Take input for the operation
    operation = input("Enter operation (+, -, *, /): ").strip()
    
    # Take input for the two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the selected operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        # Check for division by zero
        if num2 == 0:
            print("Error! Division by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation! Please use one of (+, -, *, /).")
        return
    
    # Display the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

simple_calculator()
