import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.current_input = tk.StringVar()
        self.current_input.set("")

        # Frame
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Entry widget for display
        entry = ttk.Entry(frame, textvariable=self.current_input, font=('Helvetica', 16), justify='right', state='disabled')
        entry.grid(column=0, row=0, columnspan=4, sticky=(tk.W, tk.E), ipady=10)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '⌫'  # Backspace button
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(frame, text=button, command=lambda btn=button: self.on_button_click(btn)).grid(column=col_val, row=row_val, sticky=(tk.W, tk.E, tk.N, tk.S), ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.current_input.get())
                self.current_input.set(result)
            except Exception as e:
                self.current_input.set("Error")
        elif value == '⌫':
            current_text = self.current_input.get()
            self.current_input.set(current_text[:-1])
        else:
            current_text = self.current_input.get()
            current_text += str(value)
            self.current_input.set(current_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
