from word import word

class board:
    def __init__(self):
        self.board = []

    def add_word(self, iword, icolor):
        w = word(iword, icolor)
        self.board.append( w )
        return w

    def list_words(self):
        for w in self.board:
            print(w)

"""
wordle = board()
wordle.add_word("VAGUE", "GXYYX")
wordle.add_word("STORK", "xxgxx")
wordle.add_word("CHIMP", "yxxxy")
wordle.list_words()
"""