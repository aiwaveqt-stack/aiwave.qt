"""Convert seconds to minutes and seconds"""


def to_minutes():
    """Convert seconds to minutes and remaining seconds"""
    print("Enter the time in seconds: ")
    a = int(input())

    minutes = a // 60
    seconds = a % 60

    print(f"The time is {minutes} mins {seconds} seconds.")


def main():
    to_minutes()


if __name__ == "__main__":
    main()
