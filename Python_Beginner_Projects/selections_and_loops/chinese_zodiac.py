"""Program to determine Chinese Zodiac animal based on year"""


def main():
    year = int(input("Enter a year: "))
    remainder = year % 12

    zodiac_animals = {
        0: "monkey",
        1: "rooster",
        2: "dog",
        3: "pig",
        4: "rat",
        5: "ox",
        6: "tiger",
        7: "rabbit",
        8: "dragon",
        9: "snake",
        10: "horse",
        11: "sheep"
    }

    animal = zodiac_animals.get(remainder, "unknown (invalid input)")
    print(f"Zodiac animal: {animal}")


if __name__ == "__main__":
    main()
