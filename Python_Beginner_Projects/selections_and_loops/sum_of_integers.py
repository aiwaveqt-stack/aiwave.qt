"""Program to calculate sum of first 8 integers using do-while style"""


def main():
    sum_value = 0  # Initialize sum
    i = 1  # Counter for integers

    # Python doesn't have do-while, so we use while True with break
    while True:
        sum_value += i  # Add current integer to sum
        print(f"Added {i} to sum. Current sum: {sum_value}")
        i += 1
        if i > 8:
            break

    print(f"Final sum of first 8 integers: {sum_value}")


if __name__ == "__main__":
    main()
