class Flashcard:
    def __init__(self, eng, pl):
        self.eng = eng
        self.pl = pl
        self.next_review = None
        self.interval = 1
        self.correct_streak = 0
