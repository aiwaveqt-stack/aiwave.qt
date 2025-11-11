"""
Main Interface
The main interface window with menu bar and text editor button.
"""

import tkinter as tk
from tkinter import messagebox


class MainInterface:
    """Main interface window for the text editor application."""

    def __init__(self):
        """Initialize the main interface window."""
        self.root = tk.Tk()
        self.root.title("Main Interface")
        self.root.geometry("300x150")

        # Create menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Close", command=self.close_interface)

        # Create Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # Create button panel
        button_panel = tk.Frame(self.root)
        button_panel.pack(expand=True)

        # Create text editor button
        text_editor_button = tk.Button(
            button_panel,
            text="Text Editor",
            command=self.open_text_editor
        )
        text_editor_button.pack(pady=20)

        self.root.mainloop()

    def close_interface(self):
        """Close the main interface and return to login screen."""
        self.root.destroy()
        # Import here to avoid circular dependency
        from login_screen import LoginScreen
        LoginScreen()

    def show_about(self):
        """Show about dialog."""
        messagebox.showinfo("About", "Developed by [Your Name]")

    def open_text_editor(self):
        """Open the text editor window."""
        # Import here to avoid circular dependency
        from text_editor import TextEditor
        TextEditor()


def main():
    """Main function to start the main interface."""
    MainInterface()


if __name__ == "__main__":
    main()
