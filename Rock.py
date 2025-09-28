import random

def play():
    print("🎮 Rock, Paper, Scissors Game 🎮")
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter Rock, Paper or Scissors (or 'q' to quit): ").lower()
        if user == 'q':
            print("Exiting game... 👋")
            break
        if user not in choices:
            print("⚠ Invalid choice, try again!")
            continue

        computer = random.choice(choices)
        print("Computer chose:", computer)

        if user == computer:
            print("😐 It's a Tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("🎉 You Win!")
        else:
            print("😢 You Lose!")

play()
