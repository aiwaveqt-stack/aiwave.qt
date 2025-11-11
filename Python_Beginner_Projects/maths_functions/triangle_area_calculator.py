"""Program to find area of a triangle"""


def main():
    length = int(input("Enter the length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    area = 0.5 * length * height
    print(f"The area of the triangle is: {area:.2f}")


if __name__ == "__main__":
    main()
