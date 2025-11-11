"""
Triangle Sides Finder (SOH CAH TOA)
A program to find the sides of triangles using the Pythagorean theorem.
"""

import math


class SohCahToa:
    """A class for finding triangle sides using basic trigonometry principles."""

    def menu(self):
        """Display the main menu."""
        print("---Menu ---")
        print("1. Find Sides")
        print("2. Exit")
        print("------------------------------------------------------------------------")

        self.get_menu_option()

    def get_menu_option(self):
        """
        Get and validate the menu option from the user.

        Returns:
            The selected menu option (1 or 2)
        """
        option = int(input("Enter a menu option (1 or 2): "))
        print("------------------------------------------------------------------------")

        if option < 1 or option > 2:
            print("Please enter a valid option (1 or 2).")
        else:
            self.check_menu_option(option)

        return option

    def get_side(self):
        """
        Get which side the user wants to calculate.

        Returns:
            The side to calculate (1=Adjacent, 2=Opposite, 3=Hypotenuse)
        """
        print("1. Adjacent 2. Opposite 3. Hypotenuse")
        print("------------------------------------------------------------------------")

        side = int(input("Enter the side you want to find: "))
        print("------------------------------------------------------------------------")

        if side < 1 or side > 3:
            print("Enter a valid side(1-3): ")
            print("------------------------------------------------------------------------")
        else:
            self.calculate_side(side)

        return side

    def calculate_side(self, side):
        """
        Calculate the requested side of the triangle.

        Args:
            side: Which side to calculate (1=Adjacent, 2=Opposite, 3=Hypotenuse)
        """
        if side == 1:
            print("Finding the Adjacent Side")
            print("------------------------------------------------------------------------")

            opp = float(input("Enter the opposite side: "))
            hyp = float(input("Enter the Hypotenuse: "))
            print("------------------------------------------------------------------------")

            adj = math.sqrt((hyp * hyp) - (opp * opp))
            print(f"Adjacent = {round(adj)}")
            print("------------------------------------------------------------------------")

        elif side == 2:
            print("Finding the Opposite Side")
            print("------------------------------------------------------------------------")

            adj = float(input("Enter the Adjacent side: "))
            hyp = float(input("Enter the Hypotenuse: "))
            print("------------------------------------------------------------------------")

            opp = math.sqrt((hyp * hyp) - (adj * adj))
            print(f"Opposite = {round(opp)}")
            print("------------------------------------------------------------------------")

        else:
            print("Finding the Hypotenuse Side")
            print("------------------------------------------------------------------------")

            opp = float(input("Enter the opposite side: "))
            adj = float(input("Enter the adjacent: "))
            print("------------------------------------------------------------------------")

            hyp = math.sqrt((adj * adj) + (opp * opp))
            print(f"Hypotenuse = {round(hyp)}")
            print("------------------------------------------------------------------------")

    def check_menu_option(self, option):
        """
        Process the selected menu option.

        Args:
            option: The menu option selected by the user
        """
        if option == 2:
            print("Exiting...\nThanks for using the program...")
            print("------------------------------------------------------------------------")
        else:
            self.get_side()


def main():
    """Main function to run the triangle sides finder program."""
    obj = SohCahToa()
    obj.menu()


if __name__ == "__main__":
    main()
