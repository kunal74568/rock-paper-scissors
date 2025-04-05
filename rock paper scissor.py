import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = get_winner(player_choice, computer_choice)
    print(result)

# Start the game
play_game()