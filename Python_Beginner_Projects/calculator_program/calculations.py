"""
Calculations Module
Provides basic arithmetic operations for the calculator program.
"""


class Calculations:
    """A class that performs basic arithmetic calculations."""

    def addition(self, x, y):
        """
        Add two numbers.

        Args:
            x: First number
            y: Second number

        Returns:
            The sum of x and y
        """
        return x + y

    def subtraction(self, x, y):
        """
        Subtract two numbers.

        Args:
            x: First number
            y: Second number

        Returns:
            The difference of x and y
        """
        return x - y

    def multiplication(self, x, y):
        """
        Multiply two numbers.

        Args:
            x: First number
            y: Second number

        Returns:
            The product of x and y
        """
        return x * y

    def division(self, x, y):
        """
        Divide two numbers.

        Args:
            x: First number (dividend)
            y: Second number (divisor)

        Returns:
            The quotient of x divided by y

        Raises:
            ValueError: If y is zero
        """
        if y == 0:
            raise ValueError("Division by zero is invalid")
        return x / y
