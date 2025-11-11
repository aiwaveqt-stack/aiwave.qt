class Calculator:
    """A simple calculator program"""

    def menu(self):
        """Display the menu"""
        print("\t A Simple Calculator program \n\t--Menu--")
        print(" 1. Addition")
        print(" 2. Subtraction")
        print(" 3. Multiplication")
        print(" 4. Division")
        print(" 5. Exit")
        print("Enter an option: ", end="")

    def add(self):
        """The Addition method"""
        print("\n \tAddition...")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        result = a + b
        print(f"Answer = {result}")
        return result

    def sub(self):
        """The subtraction method"""
        print("\n \tSubtraction...")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        result = a - b
        print(f"Answer = {result}")
        return result

    def mul(self):
        """The multiplication method"""
        print("\n \tMultiplication...")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        result = a * b
        print(f"Answer = {result}")
        return result

    def div(self):
        """The division method"""
        print("\n \tDivision...")
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        if b == 0:
            print("Division by zero is invalid", file=__import__('sys').stderr)
        else:
            result = a / b
            print(f"Answer = {result}")

    def exit(self):
        """A method for exit"""
        print("Exiting...")

    def main(self):
        """Main Method"""
        while True:
            self.menu()
            option = int(input())

            if option == 1:
                self.add()
            elif option == 2:
                self.sub()
            elif option == 3:
                self.mul()
            elif option == 4:
                self.div()
            elif option == 5:
                self.exit()
                break
            else:
                print("Unknown option")

            print("Do you want to continue? \n (1. Yes 2. No)")
            c = int(input())
            if c == 2:
                self.exit()
                break
            else:
                print("\n\n\n")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.main()
