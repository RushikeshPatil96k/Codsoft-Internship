# Simple calculator program

print("Welcome to the Simple Calculator!")

# Variable to control the loop
continue_calculation = 'yes'

# Loop to allow multiple operations
while continue_calculation == 'yes':
    # Asking the user to input the first number
    num1 = float(input("\nEnter the first number: "))

    # Asking the user to input the second number
    num2 = float(input("Enter the second number: "))

    # Displaying operation choices to the user
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Asking the user to choose an operation
    choice = input("Enter the number corresponding to your choice (1/2/3/4): ")

    # Performing the operation based on the user's choice
    if choice == '1':
        result = num1 + num2
        print("The result of addition is:", result)
    elif choice == '2':
        result = num1 - num2
        print("The result of subtraction is:", result)
    elif choice == '3':
        result = num1 * num2
        print("The result of multiplication is:", result)
    elif choice == '4':
        # Checking if the divisor is not zero to avoid an error
        if num2 != 0:
            result = num1 / num2
            print("The result of division is:", result)
        else:
            print("Error: Division by zero is not allowed!")
    else:
        # Handling invalid choices
        print("Invalid choice! Please try again.")

    # Asking the user if they want to continue
    continue_calculation = input("\nDo you want to perform another operation? (yes/no): ").lower()

# Ending message
print("Thank you for using the Simple Calculator!")
