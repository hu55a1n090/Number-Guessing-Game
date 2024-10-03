from Art import title
import random

# Global variable
attempts = 0

def set_difficulty():
    """Sets the difficulty level and updates the global attempts variable."""
    global attempts
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            attempts = 10
            print(f"Easy mode: You have {attempts} attempts.")
            break
        elif difficulty == "hard":
            attempts = 5
            print(f"Hard mode: You have {attempts} attempts.")
            break
        else:
            print("Invalid difficulty selected. Please try again.")

def get_guess():
    """Prompt the user for a guess and handle invalid input."""
    while True:
        try:
            guess = int(input("Guess a number: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def game():
    """Main game logic for the number guessing game."""
    global attempts
    target_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    while attempts > 0:
        guess = get_guess()

        if guess == target_number:
            print("You got it! You guessed the number.")
            return
        elif guess > target_number:
            print("You guessed too high.")
        else:
            print("You guessed too low.")
        
        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    # Out of attempts
    print(f"Oh no! You ran out of attempts. The number was {target_number}.")

# Game start
def main():
    print(title)
    print("Welcome to the number guessing game")
    
    # Set the difficulty (modifies global attempts)
    set_difficulty()

    # Start the game
    game()

if __name__ == "__main__":
    main()
