# Simple Calculator in Python
# Author: Your Name
# Description: A command-line calculator that supports basic arithmetic operations.

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def get_number(prompt):
    """Prompt the user to enter a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculator():
    """Main calculator function."""
    print("=" * 35)
    print("       Simple Python Calculator")
    print("=" * 35)

    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide),
    }

    while True:
        print("\nSelect an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Exit")
        print("-" * 35)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        num1 = get_number("Enter the first number:  ")
        num2 = get_number("Enter the second number: ")

        symbol, operation = operations[choice]

        try:
            result = operation(num1, num2)
            # Display as int if result is a whole number
            display_result = int(result) if result == int(result) else result
            print(f"\n  {num1} {symbol} {num2} = {display_result}")
        except ValueError as e:
            print(f"\n  {e}")

if __name__ == "__main__":
    calculator()
