# Simple Password Generator Program

import random  # Importing the random module


print("Welcome to the Password Generator!")

# Asking the user for the desired password length
password_length = int(input("Enter the desired length of your password: "))

# Defining possible characters for the password all alphabets capital and small along with numbers and special characters
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Generating the password
password = ""
for i in range(password_length):
    password += random.choice(characters)  # Adding a random character to the password

# Displaying the generated password
print("\nYour generated password is:", password)


print("Thank you for using the Password Generator!")


