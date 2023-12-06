import tkinter as tk
import random
import time

class TypingSpeedTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("400x300")

        self.random_text = self.get_random_text()

        self.label_instruction = tk.Label(root, text="Welcome to the Typing Speed Tester!", font=("Arial", 14))
        self.label_instruction.pack(pady=10)

        self.label_text = tk.Label(root, text=self.random_text, wraplength=380, font=("Arial", 12))
        self.label_text.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing, font=("Arial", 12))
        self.start_button.pack()

    def get_random_text(self):
        texts = [
            "Where there is a will, there is always a way.",
            "You are the greatest project you will ever work on.",
            "Believe in today for a better tomorrow .",
            "If your dreams do not scare you they are too small .",
            "The best view comes after the hardest climb."
        ]
        return random.choice(texts)

    def calculate_typing_speed(self, start_time, end_time, typed_words):
        elapsed_time = end_time - start_time
        minutes = elapsed_time / 60.0
        words_per_minute = typed_words / minutes
        return words_per_minute

    def start_typing(self):
        self.label_instruction.config(text="Type the following text:")
        self.start_button.config(state=tk.DISABLED)

        start_time = time.time()

        entry = tk.Entry(self.root, font=("Arial", 12))
        entry.pack(pady=10)

        def check_typing():
            user_input = entry.get()
            end_time = time.time()

            typed_words = len(user_input.split())
            speed = self.calculate_typing_speed(start_time, end_time, typed_words)

            accuracy = (typed_words / len(self.random_text.split())) * 100

            result_message = f"Your typing speed: {speed:.2f} words per minute\nYour typing accuracy: {accuracy:.2f}%"
            self.label_instruction.config(text=result_message)

        submit_button = tk.Button(self.root, text="Submit", command=check_typing, font=("Arial", 12))
        submit_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTesterApp(root)
    root.mainloop()
