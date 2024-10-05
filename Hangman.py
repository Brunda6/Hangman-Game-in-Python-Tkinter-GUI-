import tkinter as tk
import random

# List of words to be guessed
word_list = ["apple", "banana", "orange", "mango", "grapes", "kiwi", "cherry","watermelon", "strawberry", "pear", "peach", "plum", "lemon", "lime","papaya", "fig", "coconut", "pineapple", "blueberry", "apricot"]

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.word = random.choice(word_list)  # Pick a random word from the list
        self.guessed = set()
        self.lives = 7
        self.canvas = tk.Canvas(root, width=700, height=500, bg='white', highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=20)
        self.draw_gallows()
        self.draw_word()
        self.draw_keyboard()

    def draw_gallows(self):
        # Define an offset to shift everything to the right
        h = 157
        # Draw gallows with thicker lines
        self.canvas.create_line(20+h, 380, 120+h, 380, width=10)  # base
        self.canvas.create_line(70+h, 380, 70+h, 20, width=7)    # vertical beam
        self.canvas.create_line(70+h, 20, 200+h, 20, width=7)    # horizontal beam
        self.canvas.create_line(200+h, 20, 200+h, 50, width=7)   # rope

    def draw_word(self):
        self.word_label = tk.Label(root, text=" ".join([letter if letter in self.guessed else "_" for letter in self.word]), font=("Helvetica", 24, "bold"), bg='lightgray', fg='black')
        self.word_label.pack(pady=10)

    def draw_keyboard(self):
        keyboard_frame = tk.Frame(root, bg='gray')
        keyboard_frame.pack(pady=10)
        self.buttons = []
        row, col = 0, 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            # Increased the width of each button to 5
            button = tk.Button(keyboard_frame, text=letter, font=("Helvetica", 14, "bold"), width=5, bg='lightgray', fg='black', command=lambda letter=letter: self.guess(letter))
            button.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(button)
            col += 1
            if col > 12:  # Limit to 13 letters per row
                col = 0
                row += 1

    def guess(self, letter):
        if letter not in self.guessed:
            self.guessed.add(letter)
            if letter in self.word:
                self.word_label.config(text=" ".join([letter if letter in self.guessed else "_" for letter in self.word]))
            else:
                self.lives -= 1
                self.draw_body_part()
            if self.check_win():
                self.end_game("You win!")
            elif self.lives == 0:
                self.end_game("You lose! The word was {}".format(self.word))

    def draw_body_part(self):
        # Define an offset to shift everything to the right
        o = 150
        # Draw hangman parts with thicker lines
        if self.lives == 6:
            self.canvas.create_oval(180+o, 50, 240+o, 110, width=5)  # head
        elif self.lives == 5:
            self.canvas.create_line(210+o, 110, 210+o, 220, width=5)  # body
        elif self.lives == 4:
            self.canvas.create_line(210+o, 150, 170+o, 180, width=5)  # left arm
        elif self.lives == 3:
            self.canvas.create_line(210+o, 150, 250+o, 180, width=5)  # right arm
        elif self.lives == 2:
            self.canvas.create_line(210+o, 220, 170+o, 270, width=5)  # left leg
        elif self.lives == 1:
            self.canvas.create_line(210+o, 220, 250+o, 270, width=5)  # right leg

    def check_win(self):
        return all(letter in self.guessed for letter in self.word)

    def end_game(self, message):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        self.word_label.config(text=message, fg='black')

root = tk.Tk()
root.title("HANGMAN")
root.configure(background='lightgray')
label = tk.Label(root, text="GUESS THE FRUIT NAME", font=("Cambria", 28, "bold"), bg='lightgray', fg='black')
label.pack(pady=10)
game = HangmanGUI(root)
root.mainloop()
