# Task_001 - Rock - Paper -Scissors

import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("400x250")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.frame.pack_propagate(False)

        self.label = tk.Label(self.frame, text="Choose: Rock, Paper, or Scissors", font=("Arial", 12))
        self.label.pack()

        self.rock_button = tk.Button(self.frame, text="Rock", font=("Arial", 10, "bold"), bg="lightblue", fg="black", width=10, height=2, command=lambda: self.play_game("Rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self.frame, text="Paper", font=("Arial", 10, "bold"), bg="lightgreen", fg="black", width=10, height=2, command=lambda: self.play_game("Paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self.frame, text="Scissors", font=("Arial", 10, "bold"), bg="lightcoral", fg="black", width=10, height=2, command=lambda: self.play_game("Scissors"))
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(self.frame, text="", font=("Arial", 12))
        self.result_label.pack()

        self.score_label = tk.Label(self.frame, text=f"User Score: {self.user_score}, Computer Score: {self.computer_score}", font=("Arial", 12))
        self.score_label.pack()

    def play_game(self, user_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)

        if user_choice.capitalize() == computer_choice:
            result = "It's a tie!"
        elif (user_choice.capitalize() == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice.capitalize() == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice.capitalize() == 'Paper' and computer_choice == 'Rock'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"User chose: {user_choice}, Computer chose: {computer_choice}. {result}")
        self.score_label.config(text=f"User Score: {self.user_score}, Computer Score: {self.computer_score}")

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
