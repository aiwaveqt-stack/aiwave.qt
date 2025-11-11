"""
Read File Example
Demonstrates reading a file line by line and printing its contents.
"""


def main():
    """Read and print the contents of input.txt."""
    try:
        with open("input.txt", "r") as br:
            for line in br:
                print(line.rstrip('\n'))
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
