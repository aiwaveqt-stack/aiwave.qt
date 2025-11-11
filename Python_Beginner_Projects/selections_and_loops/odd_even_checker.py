"""Program to check if a number is odd or even"""


def main():
    number = int(input("Enter an integer: "))

    # Check even
    if number % 2 == 0:
        print("The number is even.")
    # Check odd
    if number % 2 != 0:
        print("The number is odd.")


if __name__ == "__main__":
    main()
