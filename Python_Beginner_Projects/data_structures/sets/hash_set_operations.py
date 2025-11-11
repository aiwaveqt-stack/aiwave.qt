"""
HashSet Operations Example
Demonstrates various set operations including union, intersection, and subtraction.
"""


def main():
    """Create two sets and perform various operations on them."""
    # Create the first set
    set1 = set()
    set1.add("John")
    set1.add("Mike")
    set1.add("Clement")
    set1.add("20.5")
    set1.add("Isaac")

    # Create the second set
    set2 = set()
    set2.add("John")
    set2.add("Alice")
    set2.add("Mary")
    set2.add("Clement")
    set2.add("Ama")

    # (a) Remove "20.5" from the first set
    set1.remove("20.5")
    print(f"First set after removal: {set1}")

    # (b) Print the union of the two sets
    union = set1.union(set2)
    print(f"\nUnion of sets: {union}")

    # (c) Print the intersection of the two sets
    intersection = set1.intersection(set2)
    print(f"\nIntersection of sets: {intersection}")

    # (d) Print the subtraction (set1 - set2)
    subtraction = set1.difference(set2)
    print(f"\nSubtraction (set1 - set2): {subtraction}")


if __name__ == "__main__":
    main()
