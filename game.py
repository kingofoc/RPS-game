#*****Rock, Paper and Scissors game - Chukwuebuka Kingsley******
import random

welcome = "Welcome to Rock, Paper and Scissors game"
game_options = ("""
Game options:
"R" for Rock 
"P" for Paper 
"S" for Scissors
""")

print(welcome,'\n',game_options)

R = "Rock"
P = "Paper"
S = "Scissors"

while True:
    player = input("Enter your choice: \n" ).upper()

    def user_choice():
        if player == "R":
            return R
        elif player == "P":
            return P
        elif player == "S":
            return S
        else:
            player != "R" or player != "P" or player != "S":
            return player

    def cpu_choice():
        actions = [R, P, S]
        cpu = random.choice(actions)
        return cpu

    user_choice = user_choice()
    cpu_choice = cpu_choice()

    print (f"Player [{user_choice}] : CPU [{cpu_choice}]")

    if user_choice == cpu_choice:
        print ("It is a Draw")
        continue

    elif user_choice == R:
        if cpu_choice == S:
            print("Rock crushes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_choice == P:
        if cpu_choice == R:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_choice == S:
        if cpu_choice == P:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock crushes scissors! You lose!") 
    else:
        print(f"[{user_choice}] is invalid. Please input a valid game option \n", 
        game_options)
        continue

    play_again = input("Do you want to play again? Y/N: ").upper()
    if play_again != "Y":
        break
