import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        # Password length variable
        self.length_var = tk.IntVar(value=12)

        # Character types variables
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special_chars = tk.BooleanVar(value=False)

        # Special requirements variable
        self.special_requirements_var = tk.StringVar(value='')

        # Frame
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Widgets
        ttk.Label(frame, text="Password Length:").grid(column=0, row=0, sticky=tk.W)
        length_entry = ttk.Entry(frame, textvariable=self.length_var)
        length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

        ttk.Checkbutton(frame, text="Include Lowercase", variable=self.include_lowercase).grid(column=0, row=1, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Uppercase", variable=self.include_uppercase).grid(column=0, row=2, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Digits", variable=self.include_digits).grid(column=0, row=3, sticky=tk.W)
        ttk.Checkbutton(frame, text="Include Special Characters", variable=self.include_special_chars).grid(column=0, row=4, sticky=tk.W)

        ttk.Label(frame, text="Special Requirements:").grid(column=0, row=5, sticky=tk.W)
        requirements_entry = ttk.Entry(frame, textvariable=self.special_requirements_var)
        requirements_entry.grid(column=1, row=5, sticky=(tk.W, tk.E))

        generate_button = ttk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(column=0, row=6, columnspan=2, pady=10)

        self.password_var = tk.StringVar(value="")
        password_label = ttk.Label(frame, textvariable=self.password_var)
        password_label.grid(column=0, row=7, columnspan=2, pady=10)

    def generate_password(self):
        chars = ''
        if self.include_lowercase.get():
            chars += string.ascii_lowercase
        if self.include_uppercase.get():
            chars += string.ascii_uppercase
        if self.include_digits.get():
            chars += string.digits
        if self.include_special_chars.get():
            chars += string.punctuation

        special_requirements = self.special_requirements_var.get()

        if special_requirements:
            chars += special_requirements

        length = self.length_var.get()
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
