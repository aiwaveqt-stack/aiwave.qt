"""Check if one number is a multiple of another"""


def num_multiple():
    """Check if first number is a multiple of second number"""
    first_num = int(input("Enter first Number: "))
    second_num = int(input("Enter second Number: "))

    if first_num % second_num == 0:
        print(f"{first_num} is a multiple of {second_num}")
    else:
        print(f"{first_num} is not a multiple of {second_num}")


def main():
    num_multiple()


if __name__ == "__main__":
    main()
