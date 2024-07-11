def addition(x, y):
    return x + y

def subtractraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def main():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("Choose an operation: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform the chosen operation
    if choice == '1':
        result = addition(num1, num2)
    elif choice == '2':
        result = subtractraction(num1, num2)
    elif choice == '3':
        result = multiplication(num1, num2)
    elif choice == '4':
        result = division(num1, num2)
    else:
        result = "Invalid choice. Please enter a number between 1 and 4."

    # Display the result
    print("The result is:", result)

if __name__ == "__main__":
    main()
