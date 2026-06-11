print("===== SIMPLE CALCULATOR =====")

while True:
    # Input numbers
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    # Operation menu
    print("\nChoose Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    # Perform calculation
    if choice == '1':
        result = num1 + num2
        print(f"Result = {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"Result = {result}")

    elif choice == '3':
        result = num1 * num2
        print(f"Result = {result}")

    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Result = {result}")
        else:
            print("Error: Division by zero is not allowed!")

    else:
        print("Invalid Choice!")

    # Repeat option
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Calculator Closed. Thank You!")
        break