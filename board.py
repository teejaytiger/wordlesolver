from word import word

class board:
    def __init__(self):
        self.board = []
        self.length = 0

    def add_word(self, iword, icolor):
        w = word(iword, icolor)
        self.board.append( w )
        self.length += 1
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