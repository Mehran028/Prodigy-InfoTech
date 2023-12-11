import tkinter as tk
from tkinter import ttk, messagebox
import random

class GuessingGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg="#282C34")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TFrame", background="#282C34")
        style.configure("TLabel", background="#282C34", foreground="#61dafb", font=("Arial", 16))
        style.configure("TButton", background="#61dafb", foreground="#282C34", font=("Arial", 14))

        frame = ttk.Frame(self.master)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label = ttk.Label(frame, text="Guess the Number!", style="TLabel")
        label.grid(row=0, column=0, pady=10, columnspan=2)

        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

        ttk.Label(frame, text="Enter your guess:", style="TLabel").grid(row=2, column=0, pady=10)

        self.entry = ttk.Entry(frame, font=("Arial", 14))
        self.entry.grid(row=3, column=0, pady=5)

        submit_button = ttk.Button(frame, text="Submit Guess", command=self.check_guess, style="TButton")
        submit_button.grid(row=4, column=0, pady=10)

    def check_guess(self):
        try:
            guessed_number = int(self.entry.get())
            self.attempts += 1

            if guessed_number < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guessed_number > self.secret_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations", f"You guessed the correct number {self.secret_number} in {self.attempts} attempts.")
                self.master.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameGUI(root)
    root.mainloop()
