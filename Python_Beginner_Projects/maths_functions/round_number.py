"""Program to round values using Ceil, Floor and Round"""
import math


def calculate(num1, num2):
    """Calculate and display rounding results"""
    print(f"Rounding results for {num1}:")
    print(f"Ceil: {math.ceil(num1)}")
    print(f"Floor: {math.floor(num1)}")
    print(f"Round: {round(num1)}")

    print(f"\nRounding results for {num2}:")
    print(f"Ceil: {math.ceil(num2)}")
    print(f"Floor: {math.floor(num2)}")
    print(f"Round: {round(num2)}")


def main():
    num1 = 4.53
    num2 = -3.1
    calculate(num1, num2)


if __name__ == "__main__":
    main()
