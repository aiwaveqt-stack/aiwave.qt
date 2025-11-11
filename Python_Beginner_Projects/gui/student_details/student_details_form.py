"""
Student Details Form
A form to collect and save student information (name, age, email).
"""

import tkinter as tk
from tkinter import messagebox


class StudentDetailsForm:
    """Form to collect student details and save them to a file."""

    def __init__(self):
        """Initialize the student details form window."""
        self.root = tk.Tk()
        self.root.title("Student Details")
        self.root.geometry("300x200")

        # Create panel for fields and button
        panel = tk.Frame(self.root)
        panel.pack(pady=20)

        # Name field
        name_label = tk.Label(panel, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.name_field = tk.Entry(panel, width=20)
        self.name_field.grid(row=0, column=1, padx=5, pady=5)

        # Age field
        age_label = tk.Label(panel, text="Age:")
        age_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.age_field = tk.Entry(panel, width=20)
        self.age_field.grid(row=1, column=1, padx=5, pady=5)

        # Email field
        email_label = tk.Label(panel, text="Email:")
        email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.email_field = tk.Entry(panel, width=20)
        self.email_field.grid(row=2, column=1, padx=5, pady=5)

        # Save button
        save_button = tk.Button(panel, text="Save", command=self.save_details)
        save_button.grid(row=3, column=1, padx=5, pady=15)

        self.root.mainloop()

    def save_details(self):
        """Save the student details to a file."""
        name = self.name_field.get()
        age = self.age_field.get()
        email = self.email_field.get()

        try:
            with open("student_details.txt", "w") as writer:
                writer.write(f"Name: {name}\n")
                writer.write(f"Age: {age}\n")
                writer.write(f"Email: {email}\n")
            messagebox.showinfo("Success", "Details saved successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error saving details: {str(ex)}")


def main():
    """Main function to start the student details form."""
    StudentDetailsForm()


if __name__ == "__main__":
    main()
