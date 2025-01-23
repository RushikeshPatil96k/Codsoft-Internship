# Rock-Paper-Scissors Game

import random  # Importing random module for computer's choice

# Welcome message
print("Welcome to the Rock-Paper-Scissors Game!")
print("Instructions:")
print("- Choose 'rock', 'paper', or 'scissors' to play.")
print("- Rock beats scissors, scissors beats paper, and paper beats rock.")
print("- The game will tell you if you win, lose, or tie.")
print("- You can play as many rounds as you like!\n")

play_again = "yes"  # Variable to control the game loop so thta player can play multiple rounds

while play_again == "yes":
    # Asking for the user's choice
    print("\nLet's play! Make your choice:")
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

    # Validating the user's choice
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        continue  # Restart the loop for a valid input

    # Generating computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Displaying both choices
    print(f"\n🌟 You chose: {user_choice}")
    print(f"🤖 Computer chose: {computer_choice}")

    # Determining the winner
    if user_choice == computer_choice:
        print("🔄 It's a tie! No one wins this round.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win! Great job!")
    else:
        print("💔 You lose! Better luck next time.")

    # Asking if the user wants to play again
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again not in ["yes", "no"]:
        print("Invalid input! Assuming 'no'.")
        play_again = "no"

print("\nThank you for playing Rock-Paper-Scissors! 🖐️ Goodbye!")
