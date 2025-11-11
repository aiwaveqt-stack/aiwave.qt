"""
Calculator Program Main Module
Entry point for the calculator application.
"""

from user_utils import UserUtils


def main():
    """Main function to run the calculator program."""
    user = UserUtils()
    user.display_menu()
    user.accept_menu_option()


if __name__ == "__main__":
    main()
