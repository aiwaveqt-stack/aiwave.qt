"""
Double Array Example
Demonstrates creating and populating an array with double values.
"""


def main():
    """Create an array of doubles (multiples of 2) and print them."""
    multiples_of_two = []
    for i in range(5):
        multiples_of_two.append((i + 1) * 2.0)

    for multiple in multiples_of_two:
        print(multiple)


if __name__ == "__main__":
    main()
