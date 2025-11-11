"""Program to Display maximum, minimum and absolute values in a list"""


def max_value(numbers):
    """Find maximum value in a list"""
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def min_value(numbers):
    """Find minimum value in a list"""
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def abs_value(numbers):
    """Get absolute value (first element in this implementation)"""
    abs_val = numbers[0]
    for num in numbers:
        if num == abs_val:
            abs_val = num
    return abs_val


def main():
    numbers = [-2.1, -1.5, -0.6]
    max_val = max_value(numbers)
    min_val = min_value(numbers)

    values = [-1.5, -1.5]
    abs_val = abs_value(values)

    print(f"Max: {max_val}")
    print(f"Min: {min_val}")
    print(f"Abs: {abs_val}")


if __name__ == "__main__":
    main()
