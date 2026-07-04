import random

def number_guessing_game():
    print("=" * 40)
    print("🎮 Welcome to the Number Guessing Game!")
    print("=" * 40)

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too Low! Try again.")
            elif guess > secret_number:
                print("📈 Too High! Try again.")
            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Total Attempts: {attempts}")
                break

        except ValueError:
            print("❌ Please enter a valid integer.")

# Run the game
number_guessing_game()
