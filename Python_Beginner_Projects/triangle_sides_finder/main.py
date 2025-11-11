"""
Triangle Sides Finder - Main Module
Entry point for the triangle sides finder application.
"""

from soh_cah_toa import SohCahToa


class Main:
    """Main class to run the triangle sides finder program."""

    def __init__(self):
        """Initialize the Main class with a SohCahToa object."""
        self.object = SohCahToa()

    def menu(self):
        """Display the menu and get user option."""
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
            self.object.get_side()


def main():
    """Main entry point function."""
    app = Main()
    app.menu()


if __name__ == "__main__":
    main()
