import random

options = ("rock", "paper", "scissors")
running = True

while running == True:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("TIE")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN")
    elif player == "paper" and computer == "rock":
        print("YOU WIN")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN")
    else:
        print("YOU LOSE")

    play_again = input("Play Again? Enter: y or n: ").lower()
    while play_again not in ("y", "n"):
        play_again = input("Play Again? Enter: y or n: ").lower()

    if play_again == "y":
        running = True
    elif play_again == "n":
        running = False
 

print("THANKS FOR PLAYING")



