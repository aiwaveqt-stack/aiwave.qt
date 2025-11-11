"""Simple Python program to find the sides of triangles"""
import math
import sys


class TriangleSidesCalculator:
    """Class to calculate triangle sides"""

    def __init__(self):
        """Constructor"""
        pass

    def menu(self):
        """A function to display menu"""
        print("---Menu ---")
        print("1. Find Sides")
        print("2. Exit")
        print("-" * 72)
        self.get_menu_option()

    def get_menu_option(self):
        """A function to return user menu option"""
        print("Enter a menu option (1 or 2): ")
        option = int(input())
        print("-" * 72)

        if option < 1 or option > 2:
            print("Please enter a valid option (1 or 2).")
        else:
            self.check_menu_option(option)

        return option

    def get_side(self):
        """A method to return the side to be calculated"""
        print("Enter the side you want to find: ")
        side = int(input())
        print("-" * 72)

        if side < 1 or side > 3:
            print("Enter a valid side(1-3): ")
            print("-" * 72)
        else:
            self.calculate_side(side)

        return side

    def calculate_side(self, side):
        """A method to perform side calculations"""
        if side == 1:
            print("Finding the Adjacent Side")
            print("-" * 72)

            opp = float(input("Enter the opposite side: "))
            hyp = float(input("Enter the hypotenuse: "))
            print("-" * 72)

            adj = math.sqrt((hyp * hyp) + (opp * opp))
            print(f"Adjacent = {round(adj)}")
            print("-" * 72)

        elif side == 2:
            print("Finding the Opposite Side")
            print("-" * 72)
            adj = float(input("Enter the Adjacent side: "))
            hyp = float(input("Enter the Hypotenuse: "))
            print("-" * 72)

            opp = math.sqrt((hyp * hyp) + (adj * adj))
            print(f"Opposite = {round(opp)}")
            print("-" * 72)

        else:
            print("Finding the Hypotenuse Side")
            print("-" * 72)
            opp = float(input("Enter the opposite side: "))
            adj = float(input("Enter the adjacent: "))
            print("-" * 72)

            hyp = math.sqrt((adj * adj) + (opp * opp))
            print(f"Hypotenuse = {round(hyp)}")
            print("-" * 72)

    def check_menu_option(self, option):
        """A method to validate user menu options"""
        if option == 2:
            print("Exiting...\nThanks for using the program...", file=sys.stderr)
            print("-" * 72)
        else:
            print("1. Adjacent 2. Opposite 3. Hypotenuse")
            print("-" * 72)
            self.get_side()


def main():
    """main method"""
    obj = TriangleSidesCalculator()
    obj.menu()


if __name__ == "__main__":
    main()
