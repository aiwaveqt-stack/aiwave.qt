"""
Read File with Type Detection
Reads a file and identifies the data type of each token.
"""


def get_data_type(token):
    """
    Determine the data type of a token.

    Args:
        token: The string token to analyze

    Returns:
        A string representing the data type (boolean, double, or String)
    """
    # Check for boolean
    if token.lower() in ["true", "false"]:
        return "boolean"

    # Check for double/integer
    try:
        float(token)
        return "double"
    except ValueError:
        # Not a number
        pass

    return "String"


def main():
    """Read input.txt and identify the data type of each token."""
    try:
        with open("input.txt", "r") as br:
            for line in br:
                tokens = line.split()
                for token in tokens:
                    data_type = get_data_type(token)
                    print(f"{data_type}: {token}")
                print()  # Separator between lines
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
