"""
Integer Array Example
Demonstrates creating and populating an array with integer values.
"""


def main():
    """Create an array of integers from 1 to 10 and print them."""
    numbers = []
    for i in range(10):
        numbers.append(i + 1)

    for num in numbers:
        print(num, end=" ")
    print()  # Add newline at the end


if __name__ == "__main__":
    main()
