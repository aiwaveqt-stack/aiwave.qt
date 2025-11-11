"""
User Utils Module
Handles user interaction and menu operations for the calculator program.
"""

from calculations import Calculations


class UserUtils:
    """A class that handles user interaction for the calculator."""

    def __init__(self):
        """Initialize the UserUtils with a Calculations instance."""
        self.calculate = Calculations()

    def accept_values(self):
        """
        Accept two numbers from the user.

        Returns:
            A tuple of two numbers (x, y)
        """
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        return x, y

    def display_menu(self):
        """Display the calculator menu."""
        print("---Welcome to the Calculator System---")
        print("--Menu--")
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")

    def accept_menu_option(self):
        """Accept and process the user's menu choice."""
        menu_option = int(input("Enter a menu option(1-5): "))
        self.validate_menu_option(menu_option)

    def validate_menu_option(self, menu_option):
        """
        Validate and execute the selected menu option.

        Args:
            menu_option: The menu option selected by the user (1-5)
        """
        if 1 <= menu_option <= 5:
            if menu_option == 5:
                print("Thanks for using the program.")
                return

            x, y = self.accept_values()

            if menu_option == 1:
                result = self.calculate.addition(x, y)
                print(f"Answer = {result}")
            elif menu_option == 2:
                result = self.calculate.subtraction(x, y)
                print(f"Answer = {result}")
            elif menu_option == 3:
                result = self.calculate.multiplication(x, y)
                print(f"Answer = {result}")
            elif menu_option == 4:
                try:
                    result = self.calculate.division(x, y)
                    print(f"Answer = {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("Invalid input...try again")
