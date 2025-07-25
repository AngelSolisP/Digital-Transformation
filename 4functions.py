def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides the first number by the second and returns the result."""
    # Handle division by zero
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    """Main function to run the calculator program."""
    print("Welcome to the basic calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return  # Exit the function if input is not a number

    op = input("Enter the operation (+, -, *, /): ")

    result = 0
    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operation. Please try again.")
        return  # Exit the function for invalid operation

    print(f"The result is: {result}")

# This ensures the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()