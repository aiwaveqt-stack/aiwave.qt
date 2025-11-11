"""BMI Calculator Program"""
import math


def main():
    # Ask the user for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = weight / math.pow(height, 2)

    # Determine health indication
    if bmi < 18.5:
        health_indication = "Underweight"
    elif bmi < 25.0:
        health_indication = "Normal"
    elif bmi < 30.0:
        health_indication = "Overweight"
    else:
        health_indication = "Obese"

    # Display BMI and health indication
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your health indication is: {health_indication}")


if __name__ == "__main__":
    main()
