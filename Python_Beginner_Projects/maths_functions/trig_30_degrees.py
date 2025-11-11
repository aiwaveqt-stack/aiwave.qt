"""Calculate trigonometric values for 30 degrees"""
import math


def convertor(angle):
    """Convert angle to radians and calculate trig values"""
    degrees = angle
    radian = math.radians(degrees)

    cos_value = math.cos(radian)
    sin_value = math.sin(radian)
    tan_value = math.tan(radian)

    print("The Trigonometric Values For 30 degrees")
    print(f"cos({degrees})= {cos_value:.4f}")
    print(f"sin({degrees})= {sin_value:.4f}")
    print(f"tan({degrees})= {tan_value:.4f}")


def main():
    angle = 30.0  # Setting angle to 30 degrees
    convertor(angle)


if __name__ == "__main__":
    main()
