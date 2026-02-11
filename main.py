import tkinter as tk
from models import Flashcard
from spaced_repetition import update_card
from stats import calculate_stats
import json



class FlashcardsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards C1 Trainer")

        self.cards = []
        self.current_card = None

        self.load_cards()
        self.create_widgets()
        self.show_next_card()



    def load_cards(self):
        with open("data/slowka_c1.txt", "r", encoding="utf-8") as f:
            for line in f:
                eng, pl = line.strip().split("   ")
                self.cards.append(Flashcard(eng, pl))



    def create_widgets(self):
        self.word_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.word_label.pack(pady=40)

        self.show_button = tk.Button(self.root, text="Show Translation", command=self.show_translation)
        self.show_button.pack()

        self.know_button = tk.Button(self.root, text="I know", command=lambda: self.answer(True))
        self.know_button.pack(side="left", padx=20)

        self.dont_know_button = tk.Button(self.root, text="I don't know", command=lambda: self.answer(False))
        self.dont_know_button.pack(side="right", padx=20)



    def answer(self, was_correct):
        update_card(self.current_card, was_correct)
        self.save_progress()
        self.show_next_card()



    def save_progress(self):
        data = {}
        for card in self.cards:
            data[card.eng] = {
                "interval": card.interval,
                "next_review": str(card.next_review),
                "correct_streak": card.correct_streak
            }

        with open("user_progress.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()
