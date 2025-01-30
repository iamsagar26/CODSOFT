def simple_calculator():
    print("Welcome to the Simple Calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("Enter the number respectively to the operation (1/2/3/4): ")
        
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '4':
            if num2 == 0:
                print("Error: Division by zero is not defined.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid operation . Enter a valid operation.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

simple_calculator()

