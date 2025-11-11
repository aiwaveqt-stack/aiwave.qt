"""Celsius to Fahrenheit Converter"""


def main():
    # Ask the user for a Celsius temperature
    celsius = float(input("Enter a temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (9.0 / 5.0) * celsius + 32.0

    # Display the result
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()
