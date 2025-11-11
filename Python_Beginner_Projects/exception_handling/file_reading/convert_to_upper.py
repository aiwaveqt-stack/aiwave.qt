"""
Convert to Upper Case
Reads a file and writes its content in uppercase to another file.
"""


def main():
    """Read input.txt and write its content in uppercase to Out.txt."""
    try:
        with open("input.txt", "r") as br, open("Out.txt", "w") as bw:
            for line in br:
                bw.write(line.upper())
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
