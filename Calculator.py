# This program simulates a simple calculator using if-elif-else statements.

def calculator():
    
    print("--- Simple Calculator ---")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("-------------------------")

    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))

        # Get the second number from the user
        num2 = float(input("Enter the second number: "))

    except ValueError:
        
        print("\nError: Invalid input. Please enter only numbers.")
        return

    # Get the operation choice from the user
    choice = input("Enter operator choice (+, -, *, /): ")
    print("-" * 25)

    var = None

    if choice == '+':
        # Addition
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")

    elif choice == '-':
        # Subtraction
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")

    elif choice == '*':
        # Multiplication
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")

    elif choice == '/':
        # Division
        
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")

    else:
       
        print("Error: Invalid operator choice. Please enter one of +, -, *, /.")


if __name__ == "__main__":
    
    calculator()
    
