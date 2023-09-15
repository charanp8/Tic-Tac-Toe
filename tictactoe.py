import random

while True:
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    x = input("Rock, Paper, or Scissors? ")

    if x == computer:
        print("It's a tie")
    elif x == "Rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif x == "Scissors":
        if computer == "Rock":
            print("You lose!")
        else:
            print("You win!")
    elif x == "Paper":
        if computer == "Rock":
            print("You win!")
        else:
            print("You lose!")

