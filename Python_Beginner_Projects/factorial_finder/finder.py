"""Factorial Finder Program"""


class Finder:
    """Factorial Finder class"""

    def __init__(self):
        self.get_user_option()

    def get_user_option(self):
        """Get user option"""
        option = int(input("Do you want to continue (1. Yes 2. No):  "))
        self.validate_user_option(option)
        return option

    def validate_user_option(self, option):
        """Validate user option"""
        if option != 1 and option != 2:
            print("Please enter a valid option 1 or 2")
            self.get_user_option()
        else:
            if option == 1:
                self.get_user_number()
            else:
                print("Thanks for using the program...Bye!")

    def get_user_number(self):
        """Get number from user"""
        number = int(input("Enter the number to find the factorial: "))
        self.validate_number(number)

    def validate_number(self, number):
        """Validate the number"""
        if number <= 0:
            print("Number must be greater than zero! ")
            self.get_user_number()
        else:
            answer = self.factorial(number)
            print(f"{number}! = {answer:,}")
            self.get_user_option()

    def factorial(self, number):
        """Calculate factorial recursively"""
        if number == 1:
            return 1
        else:
            return number * self.factorial(number - 1)


if __name__ == "__main__":
    finder = Finder()
