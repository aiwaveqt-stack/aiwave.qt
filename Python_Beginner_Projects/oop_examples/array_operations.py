"""Array Operations with 2D arrays"""
from array_sum_calculator import calculate_sum


def print_array(array):
    """Method to print 2D array"""
    for row in array:
        for num in row:
            print(f"{num:<8.2f}", end="")  # Format to 2 decimal places
        print()


def main():
    # Create 2D arrays of different sizes
    array1 = [
        [1.1, 2.2, 3.3],
        [4.4, 5.5, 6.6]
    ]

    array2 = [
        [7.7, 8.8],
        [9.9, 10.1],
        [11.11, 12.12]
    ]

    # Print arrays
    print("Array 1:")
    print_array(array1)

    print("\nArray 2:")
    print_array(array2)

    # Calculate and display sums
    print(f"\nSum of Array 1: {calculate_sum(array1)}")
    print(f"Sum of Array 2: {calculate_sum(array2)}")


if __name__ == "__main__":
    main()
