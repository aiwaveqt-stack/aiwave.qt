"""String and Character Operations in Python"""


def main():
    # 1. Printing Statements
    print("John said 'Python is fun and easy'")
    print('John said "Python is fun and easy"')

    # 2. Converting Numeric Types to Characters
    char1 = chr(99)  # 'c'
    char2 = chr(225)  # 'á'

    print(f"\nCharacter for 99: {char1}")
    print(f"Character for 225: {char2}")

    # 3. Converting Characters to Integers (ASCII values)
    ch1 = 'A'
    ch2 = '!'
    ch3 = '*'
    ch4 = 'i'

    int1 = ord(ch1)  # ASCII value of 'A'
    int2 = ord(ch2)  # ASCII value of '!'
    int3 = ord(ch3)  # ASCII value of '*'
    int4 = ord(ch4)  # ASCII value of 'i'

    print(f"\nASCII value of 'A': {int1}")
    print(f"ASCII value of '!': {int2}")
    print(f"ASCII value of '*': {int3}")
    print(f"ASCII value of 'i': {int4}")

    # Optional: Get numeric value of a character
    ch = '5'
    numeric_value = int(ch)  # 5

    print(f"\nNumeric value of '5': {numeric_value}")


if __name__ == "__main__":
    main()
