"""
Login Screen
A simple login screen for the text editor application using tkinter.
"""

import tkinter as tk
from tkinter import messagebox
from main_interface import MainInterface


class LoginScreen:
    """Login screen with username and password validation."""

    def __init__(self):
        """Initialize the login screen window."""
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x200")

        # Create username label and entry
        username_label = tk.Label(self.root, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.username_field = tk.Entry(self.root, width=20)
        self.username_field.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Create password label and entry
        password_label = tk.Label(self.root, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.password_field = tk.Entry(self.root, width=20, show="*")
        self.password_field.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Create button frame
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)

        # Create login button
        login_button = tk.Button(button_frame, text="Login", command=self.login)
        login_button.pack(side=tk.LEFT, padx=5)

        # Create reset button
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset)
        reset_button.pack(side=tk.LEFT, padx=5)

        self.root.mainloop()

    def login(self):
        """Handle login button click."""
        username = self.username_field.get()
        password = self.password_field.get()

        if username == "admin" and password == "password":
            # Login successful
            messagebox.showinfo("Success", f"Welcome, {username}")
            self.root.destroy()
            MainInterface()
        else:
            # Login failed
            messagebox.showerror("Error", "Incorrect username or password")

    def reset(self):
        """Handle reset button click - clear all fields."""
        self.username_field.delete(0, tk.END)
        self.password_field.delete(0, tk.END)


def main():
    """Main function to start the login screen."""
    LoginScreen()


if __name__ == "__main__":
    main()
