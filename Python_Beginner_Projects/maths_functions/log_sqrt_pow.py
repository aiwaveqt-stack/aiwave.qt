"""Program to display:
- Natural Log of 45
- Square root of 29
- 5 Exponent of 65
"""
import math


def natural_log(value):
    """Calculate natural logarithm"""
    return math.log(value)


def square_root(value):
    """Calculate square root"""
    return math.sqrt(value)


def power_of(base, exponent):
    """Calculate power"""
    return math.pow(base, exponent)


def main():
    value1 = 45
    value2 = 29
    base = 5
    exponent = 65

    log_value = natural_log(value1)  # value = 45
    root_value = square_root(value2)  # value = 29
    power_value = power_of(base, exponent)  # base = 5, exponent = 65

    # displaying the various answers
    print(f"Natural log of ({value1}) = {log_value:.4f}")
    print(f"Square root of ({value2}) = {root_value:.4f}")
    print(f"{base} exponent {exponent} = {power_value:.2f}")


if __name__ == "__main__":
    main()
