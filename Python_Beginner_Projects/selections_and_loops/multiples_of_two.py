"""Program to display multiples of 2"""


def main():
    i = 1  # Counter for multiples
    while i <= 5:
        multiple = 2 * i
        print(f"Multiple {i} of 2: {multiple}")
        i += 1


if __name__ == "__main__":
    main()
