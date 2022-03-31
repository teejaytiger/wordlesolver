from letter import letter
from colorama import init, Fore, Back, Style
init(convert=True)

class word:
    def __init__(self, word, colors):
        w = word.upper()
        c = colors.upper()
        self.alpha = word
        self.word = [letter(a, b) for a, b in zip( list(w), list(c) ) ]
        self.clrs = {'G':Fore.BLACK+Back.GREEN, 'Y':Fore.BLACK+Back.YELLOW, None:Fore.RESET+Back.RESET}

    def __str__(self):
        s = ""
        for l in self.word:
            s+= self.clrs[l.color] + " " + l.alpha + " " +  Style.RESET_ALL
        return s