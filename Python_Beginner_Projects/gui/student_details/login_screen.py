"""
Login Screen for Student Details
A simple login screen that validates credentials and opens the student details form.
"""

import tkinter as tk
from tkinter import messagebox
from student_details_form import StudentDetailsForm


class LoginScreen:
    """Login screen with username and password validation."""

    def __init__(self):
        """Initialize the login screen window."""
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x150")

        # Create fields panel
        fields_panel = tk.Frame(self.root)
        fields_panel.pack(pady=20)

        # Username field
        username_label = tk.Label(fields_panel, text="Username:")
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.username_field = tk.Entry(fields_panel, width=20)
        self.username_field.grid(row=0, column=1, padx=5, pady=5)

        # Password field
        password_label = tk.Label(fields_panel, text="Password:")
        password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.password_field = tk.Entry(fields_panel, width=20, show="*")
        self.password_field.grid(row=1, column=1, padx=5, pady=5)

        # Create buttons panel
        buttons_panel = tk.Frame(self.root)
        buttons_panel.pack(pady=10)

        # Login button
        login_button = tk.Button(buttons_panel, text="Login", command=self.login)
        login_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        reset_button = tk.Button(buttons_panel, text="Reset", command=self.reset)
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
            StudentDetailsForm()
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
