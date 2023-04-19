import random

play_again = True

while play_again:

    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ")

    if user_action != "R" and user_action != "P" and user_action != "S":
        print("Oops! Please enter a valid choice! R, P or S...")
        continue

    if user_action == "R":
        user_action = 0
    elif user_action == "P":
        user_action = 1
    else:
        user_action = 2

    computer_action = random.randint(0, 2)

    choices = ["Rock", "Paper", "Scissors"]

    print(f"\nYou chose {choices[user_action]}, computer chose {choices[computer_action]}.\n")

    if user_action == computer_action:
        print(f"Both players selected {choices[user_action]}. It's a tie!")
    elif user_action == 0:
        if computer_action == 2:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == 1:
        if computer_action == 0:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == 2:
        if computer_action == 1:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n):")

    if play_again.lower() == "n":
        play_again = False