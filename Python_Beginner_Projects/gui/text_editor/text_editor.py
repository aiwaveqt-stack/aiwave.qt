"""
Text Editor
A simple text editor with file open/save and font customization features.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import font as tkfont


class TextEditor:
    """A simple text editor with basic file operations and font customization."""

    def __init__(self):
        """Initialize the text editor window."""
        self.root = tk.Tk()
        self.root.title("Text Editor")
        self.root.geometry("600x400")

        # Create menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Create Font Size menu
        font_size_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Font Size", menu=font_size_menu)
        font_size_menu.add_command(label="12", command=lambda: self.set_font_size(12))
        font_size_menu.add_command(label="14", command=lambda: self.set_font_size(14))

        # Create Font Type menu
        font_type_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Font Type", menu=font_type_menu)
        font_type_menu.add_command(label="Arial", command=lambda: self.set_font_type("Arial"))
        font_type_menu.add_command(label="Times New Roman", command=lambda: self.set_font_type("Times New Roman"))

        # Create text area with scrollbar
        self.text_area = scrolledtext.ScrolledText(
            self.root,
            width=40,
            height=20,
            wrap=tk.WORD,
            font=("Arial", 12)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create button panel
        button_panel = tk.Frame(self.root)
        button_panel.pack(side=tk.BOTTOM, pady=5)

        # Create open button
        open_button = tk.Button(
            button_panel,
            text="Open Text File",
            command=self.open_file
        )
        open_button.pack(side=tk.LEFT, padx=5)

        # Create save button
        save_button = tk.Button(
            button_panel,
            text="Save To Text File",
            command=self.save_file
        )
        save_button.pack(side=tk.LEFT, padx=5)

        self.root.mainloop()

    def open_file(self):
        """Open a text file and display its contents in the text area."""
        file_path = filedialog.askopenfilename(
            title="Open Text File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Error", f"Error opening file: {str(e)}")

    def save_file(self):
        """Save the text area contents to a file."""
        file_path = filedialog.asksaveasfilename(
            title="Save To Text File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {str(e)}")

    def set_font_size(self, size):
        """
        Change the font size of the text area.

        Args:
            size: The new font size
        """
        current_font = tkfont.Font(font=self.text_area['font'])
        font_family = current_font.actual()['family']
        self.text_area.config(font=(font_family, size))

    def set_font_type(self, font_type):
        """
        Change the font type of the text area.

        Args:
            font_type: The new font family name
        """
        current_font = tkfont.Font(font=self.text_area['font'])
        font_size = current_font.actual()['size']
        self.text_area.config(font=(font_type, font_size))


def main():
    """Main function to start the text editor."""
    TextEditor()


if __name__ == "__main__":
    main()
