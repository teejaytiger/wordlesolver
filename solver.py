from mimetypes import common_types
from board import board
import pickle
import random
import difflib

# import the word as a set
with open("wordledict.pickle", 'rb') as pickledict:
    valid_set = pickle.load(pickledict)

# import the common set
with open("common.pickle", 'rb') as pickledict:
    common_words = pickle.load(pickledict)

# create the board
b = board()

# suggest starters
starters = ["React","Adieu","Later","Sired","Tears","Alone","Arise","About","Atone","Irate","Snare","Cream","Paint","Worse","Sauce","Anime","Prowl","Roast","Drape","Media"]
cur_choice = random.choice(starters).upper()

print("I suggest you start with {}.".format(cur_choice))

def ask():
    pat = input("What did it return?\n(format: x for blank, y for yellow, g for green, no spaces\n")
    # check input
    if len(pat)==5:
        if pat.upper() == "GGGGG":
            return None
        return str(pat).upper()
    else:
        print("sorry, that wasn't valid\n")
        ask()

def eliminate_choices(vs, word):
    lowc = 1
    lowunc = 1
    wc = None
    wunc = None
    r = False
    ref = list(vs)
    for i in ref:
        r = False
        # iterate through the valid word list
        for letter, comp in zip( word.word, list(i) ):
            c = letter.color
            if c:
                if c=="G":
                    # remove words that don't have green letters in the same column
                    if comp != letter.alpha:
                        if i in vs: vs.remove(i)
                        r = True
                if c=="Y":
                    # remove words that do not contain yellow letters
                    if not (letter.alpha in i):
                        if i in vs: vs.remove(i)
                        r = True
                    # remove words that have yellow letters in the same column
                    if comp == letter.alpha:
                        if i in vs: vs.remove(i)
                        r = True
            else:
                # remove words that contain black letters
                if letter.alpha in i:
                    if i in vs: vs.remove(i)
                    r = True
        if not r:
            if i in common_words:
                # check for common words first, get highest semantic distance from current (maximize letter usage)
                d = difflib.SequenceMatcher(None, i, word.word).ratio()
                if d < lowc: 
                    d = lowc
                    wc = i
            else: 
                # do the same for uncommon words in case common words are exhausted
                d = difflib.SequenceMatcher(None, i, word.word).ratio()
                if d < lowunc: 
                    d = lowunc
                    wunc = i
        w = wunc
        if wc: w = wc
    return w, vs

def loop(cur_choice, valid_set):

    # get word feedback
    pattern = ask()
    if pattern:
        word = b.add_word(cur_choice, pattern)
        b.list_words()

        # eliminate choices
        next_guess, valid_set = eliminate_choices(valid_set, word)

        # suggest next word
        print("{} remaining words to choose from".format(len(valid_set)))
        cur_choice = random.choice(list(valid_set)).upper()
        print("I suggest {} as your next word".format(next_guess))
        loop(next_guess, valid_set)
    else:
        b.add_word(cur_choice, "GGGGG") 
        b.list_words()
        return

loop(cur_choice, valid_set)
