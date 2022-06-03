import random

welcome = "Welcome to Rock, Paper and Scissors game"
print(welcome)


while True:

    user_action = input('''
    Enter a choice - (R for Rock, P for Paper or S for Scissors): 
    ''').upper()

    actions = ["R", "P", "S"]
    computer_action = random.choice(actions)

    print(f"You choose[{user_action}] : CPU choose[{computer_action}]")

    if user_action == computer_action:
        print(f"Both Players Selected {user_action}. It is a draw!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock crushes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")

    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")

    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock crushes scissors! You lose!")
    
    elif user_action != "R" or user_action !="P" or user_action != "S":
        print(f"[{user_action}] is not a valid game option. Input a valid game option")

        continue

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != "Y":
        break


