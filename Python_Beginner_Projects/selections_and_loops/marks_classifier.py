"""Program to classify marks"""


def main():
    mark = float(input("Enter your marks: "))

    if mark >= 80.0:
        print("First class")
    elif mark >= 70.0:
        print("Second class Upper")
    elif mark >= 60.0:
        print("Second class lower")
    elif mark >= 50.0:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    main()
