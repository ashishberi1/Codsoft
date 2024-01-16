def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter operation (1-4): "))
        if choice < 1 or choice > 4:
            print("Invalid choice")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            operation = "Addition"
        elif choice == 2:
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == 3:
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == 4:
            result = divide(num1, num2)
            operation = "Division"

        print(f"{operation} result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
