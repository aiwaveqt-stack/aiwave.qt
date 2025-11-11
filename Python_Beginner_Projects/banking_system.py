import tkinter as tk
from tkinter import messagebox, simpledialog


class BankingSystem:
    """A dialog calculator program using tkinter"""

    def __init__(self):
        self.input = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def menu(self):
        """Class Menu method"""
        messagebox.showinfo("Calculator", "A Simple Calculator using Dialog.")
        menu_text = "\t Menu: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit"
        self.input = simpledialog.askinteger("Menu", menu_text + "\n Enter an option:")

    def add(self):
        """Class Addition Method"""
        messagebox.showinfo("Operation", "\t Addition")
        self.x = float(simpledialog.askstring("Input", "Enter First Number:"))
        self.y = float(simpledialog.askstring("Input", "Enter Second Number:"))
        self.z = self.x + self.y
        messagebox.showinfo("Result", f"{self.x} + {self.y} = {self.z}")

    def sub(self):
        """Class Subtraction method"""
        messagebox.showinfo("Operation", "\t Subtraction")
        self.x = float(simpledialog.askstring("Input", "Enter First Number:"))
        self.y = float(simpledialog.askstring("Input", "Enter Second Number:"))
        self.z = self.x - self.y
        messagebox.showinfo("Result", f"{self.x} - {self.y} = {self.z}")

    def mul(self):
        """Class Multiplication method"""
        messagebox.showinfo("Operation", "\t Multiplication")
        self.x = float(simpledialog.askstring("Input", "Enter First Number:"))
        self.y = float(simpledialog.askstring("Input", "Enter Second Number:"))
        self.z = self.x * self.y
        messagebox.showinfo("Result", f"{self.x} x {self.y} = {self.z}")

    def div(self):
        """Class Division method"""
        messagebox.showinfo("Operation", "\t Division")
        self.x = float(simpledialog.askstring("Input", "Enter First Number:"))
        self.y = float(simpledialog.askstring("Input", "Enter Second Number:"))

        # Validating the division method, in case user input for y = 0
        if self.y == 0:
            messagebox.showerror("Error", "Division by zero is invalid!")
        else:
            self.z = self.x / self.y
            messagebox.showinfo("Result", f"{self.x} / {self.y} = {self.z}")

    def exit_program(self):
        """A class method to quit the program"""
        messagebox.showinfo("Exit", "You closed the program, goodbye!")

    def main(self):
        """Main method"""
        while True:
            self.menu()

            # A list of conditions to validate user inputs for menu options
            if self.input == 1:
                self.add()
            elif self.input == 2:
                self.sub()
            elif self.input == 3:
                self.mul()
            elif self.input == 4:
                self.div()
            elif self.input == 5:
                self.exit_program()
                break
            else:
                # An else statement for error handling
                messagebox.showerror("Error", "Your input was invalid. Please try again.")

            # Global variable for program continuation
            next_input = simpledialog.askinteger(
                "Continue", "Do you want to continue: (1.Yes / 2.No)"
            )
            if next_input == 2:
                self.exit_program()
                break

        self.root.destroy()


if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main()
