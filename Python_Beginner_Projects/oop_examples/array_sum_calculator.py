"""Array Sum Calculator Module"""


def calculate_sum(array):
    """Method to calculate sum of 2D array"""
    total = 0.0
    for row in array:
        for num in row:
            total += num
    return total
