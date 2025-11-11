"""Random Guessing Game"""
import random
import sys


class Game:
    """The Game class"""

    def __init__(self):
        """A default constructor to initialize the Game class"""
        self.guess = 0
        print("---Menu---")
        print("-" * 57)
        print("1. Play")
        print("2. Quit")
        print("-" * 57)
        self.get_user_option()

    def get_user_option(self):
        """A method to return and validate user option value"""
        print("Enter a choice (1 or 2): ")
        choice = int(input())
        print("-" * 57)

        if choice != 1 and choice != 2:
            print("Please enter a valid choice (1 or 2).")
            print("-" * 57)
        else:
            self.check_choice(choice)

        return choice

    def check_choice(self, choice):
        """A method that checks the choices of user input"""
        if choice == 1:
            self.play_game()
        else:
            print("-" * 57)
            print("Thanks for using the program...")
            print("-" * 57)

    def play_game(self):
        """Play the game"""
        self.get_user_guess()

    def get_user_guess(self):
        """A method that returns user guesses"""
        print("Please guess a number from (1 - 50) or (0 to quit)")
        user_guess = int(input())
        print("-" * 57)

        if user_guess < 0 or user_guess > 50:
            print("Guess must be between 1 to 50", file=sys.stderr)
        else:
            guess = self.random_guess()
            self.check_guess(user_guess, guess)

        return user_guess

    def check_guess(self, user_guess, guess):
        """Check if the user's guess is correct"""
        while True:
            if user_guess == 0:
                print("Thanks for playing....", file=sys.stderr)
                break

            elif user_guess < guess:
                print("Your guess is low. Try again!", file=sys.stderr)
            elif user_guess > guess:
                print("Your guess is high. Try again!", file=sys.stderr)
            else:
                print("Your guess was correct!", file=sys.stderr)
                break

            print("-" * 57)
            print(f"The number was {guess}", file=sys.stderr)
            print("-" * 57)

            self.get_user_guess()

    def random_guess(self):
        """A method that returns the random guess"""
        guess = random.randint(1, 50)
        return guess


if __name__ == "__main__":
    game = Game()
