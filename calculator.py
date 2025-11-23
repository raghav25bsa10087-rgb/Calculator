def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def show_menu():
    print("\n===== Simple Python Calculator =====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("===================================")


def main():
    print("Welcome to the Python Calculator!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Exiting... Thank you for using the calculator!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice! Please select a valid option (1-5).")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        try:
            if choice == "1":
                result = add(num1, num2)
                op = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op = "*"
            else:  # choice == "4"
                result = divide(num1, num2)
                op = "/"

            print(f"\nResult: {num1} {op} {num2} = {result}\n")

        except ZeroDivisionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
