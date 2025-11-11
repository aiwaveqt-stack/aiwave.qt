"""Program to find the division of two numbers"""


def divide(num1, num2):
    """Divide two numbers"""
    if num2 == 0:
        print("Division by zero is invalid")
    return num1 / num2


def main():
    num1 = 2.0
    num2 = 6.0
    result = divide(num1, num2)

    print(f"{num1}/{num2}= {result:.2f}")


if __name__ == "__main__":
    main()
