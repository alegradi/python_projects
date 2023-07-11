import random
from art import logo

# Global variables
EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

print(logo)

# Generate random integer
for _ in range(1):
    random_number = random.randint(1, 100)
    ## Debug printing
    # print("The 'random_number is: " + str(random_number))

player_difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
if player_difficulty == "easy":
    guess_remaining = EASY_DIFFICULTY
elif player_difficulty == "hard":
    guess_remaining = HARD_DIFFICULTY
else:
    print("You've entered garbage as your choice.")
    guess_remaining = 0

def compare_numbers(target_num, guess):
    """Function to compare the guess to the target number."""
    global game_over
    if target_num < guess:
        print("Too high!")
    elif target_num > guess:
        print("Too low!")
    else:
        print("You're bang on! Congratulations!")
        print("Game Over!")
        game_over = True

game_over = False

while not game_over:
    if guess_remaining == 0:
        print("You are out of guesses!")
        print("Game over!")
        game_over = True
    else:
        guess_remaining -= 1
        print("You have " + str(guess_remaining + 1) + " guesses remaining.")
        guess = int(input("\nEnter your guess: "))
        compare_numbers(random_number, guess)
