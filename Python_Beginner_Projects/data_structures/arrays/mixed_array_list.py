"""
Mixed ArrayList Example
Demonstrates using a list to store different types of objects (strings and numbers).
"""


def main():
    """Create a mixed list with strings and a number, then demonstrate removal."""
    mixed_list = []
    mixed_list.append("John")
    mixed_list.append("Mike")
    mixed_list.append("Ama")
    mixed_list.append(20.34)
    mixed_list.append("Daniel")

    print(f"Initial size of the list: {len(mixed_list)}")
    print(f"Initial content of the list: {mixed_list}")

    # Remove 20.34 from the list
    mixed_list.remove(20.34)

    print(f"Size of the list after removal: {len(mixed_list)}")
    print(f"Content of the list after removal: {mixed_list}")


if __name__ == "__main__":
    main()
