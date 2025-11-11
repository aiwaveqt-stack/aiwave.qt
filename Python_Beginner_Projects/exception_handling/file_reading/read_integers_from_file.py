"""
Read Integers from File
Reads integers from a file and stores them in a list.
"""


def read_integers_from_file(filename):
    """
    Read integers from a file.

    Args:
        filename: The name of the file to read

    Returns:
        A list of integers, or None if an error occurs
    """
    integer_list = []

    try:
        with open(filename, "r") as br:
            for line in br:
                integer_list.append(int(line.strip()))
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing integer: {e}")
        return None

    return integer_list


def main():
    """Read integers from integers.txt and print them."""
    filename = "integers.txt"
    integers = read_integers_from_file(filename)

    if integers is not None:
        for integer in integers:
            print(integer)


if __name__ == "__main__":
    main()
