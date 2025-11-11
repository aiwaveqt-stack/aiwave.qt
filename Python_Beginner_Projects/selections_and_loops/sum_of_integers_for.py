"""Program to calculate sum of first 10 integers using for loop"""


def main():
    sum_value = 0  # Initialize sum
    for i in range(1, 11):
        sum_value += i  # Add current integer to sum
        print(f"Added {i} to sum. Current sum: {sum_value}")
    print(f"Final sum of first 10 integers: {sum_value}")


if __name__ == "__main__":
    main()
