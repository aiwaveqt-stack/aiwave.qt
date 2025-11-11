"""
Student Marks Map Example
Demonstrates using a dictionary to store student index numbers and their marks.
"""


def main():
    """Create a dictionary to store student index numbers and marks, then print them."""
    # Create a dictionary to store student index numbers and marks
    student_marks = {}

    # Insert student index numbers and marks into the dictionary
    student_marks["42200213"] = 89
    student_marks["42225413"] = 65
    student_marks["42234513"] = 89
    student_marks["42233413"] = 78

    # Print out the content of the dictionary
    print("Student Marks:")
    for index in student_marks.keys():
        print(f"Index: {index}, Mark: {student_marks[index]}")


if __name__ == "__main__":
    main()
