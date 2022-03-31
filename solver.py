from mimetypes import common_types
from board import board
import pickle
import random
import difflib
import re

# import the word as a set
with open("wordledict.pickle", 'rb') as pickledict:
    valid_set = pickle.load(pickledict)

# import the common set
with open("common.pickle", 'rb') as pickledict:
    common_words = pickle.load(pickledict)

def new_board():
    # create the board
    b = board()

    # suggest starters
    starters = ["React","Adieu","Later","Sired","Tears","Alone","Arise","About","Atone","Irate","Snare","Cream","Paint","Worse","Sauce","Anime","Prowl","Roast","Drape","Media"]
    cur_choice = random.choice(starters).upper()
    print("I suggest you start with {}.".format(cur_choice))
    return cur_choice, b

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
    low = 1
    w = None
    r = False
    ref = list(vs)
    for i in ref:
        r = False
        # iterate through the valid word list
        pos = 0
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
                #TODO: modify this to except words which have duplicate letter as yellow or green
                if letter.alpha in i:
                    remove = True
                    for j in word.word:
                        if j.alpha==letter.alpha and (j.color=="G" or j.color=="Y"): # don't remove condition
                            remove = False
                    if i in vs and remove: 
                        vs.remove(i)
                        r = True
            pos += 1

        if not r:
            # TODO: at this step, there's a tendency to pick words with double letters, and I want to discourage that somehow
            # check for common words first, get highest semantic distance from current (maximize letter usage)
            d = difflib.SequenceMatcher(None, i, word.alpha).ratio()
            if any(s==t for s, t in zip(i, i[1:])): d = d/.3 # maybe penalizes double letters? idk
            if len(set(i))==5: d = d*.2 # small bonus for words with distinct letters
            if i in common_words: d = d*.2 # small bonus for being a common word
            # print("{0:.2f} : {1}".format(d, i)) # uncomment to get scores
            if d < low: 
                low = d
                w = i
    return w, vs, d

def board_builder():
    b = board()
    b.add_word("WORDS", "XYGGX")
    x = True
    print("Welcome to the wordle builder!\n - Input workds and their patterns from an existing game in the following format:")
    print("\nWORDS xyggx")
    print("This will generate:")
    b.list_words()
    b = board()
    while b.length < 6:
        i = input("Add a word, or Enter to finish: ")
        if not i: return cur_choice, b
        l = i.split(" ")
        try:
            cur_choice = b.add_word(l[0].upper(), l[1].upper())
        except:
            print("Something happened, try again.")
    return cur_choice, b

def loop(valid_set, board=None, cur_choice=None):
    # get word feedback
    b = board
    if not cur_choice:
        if b:
            #start fresh
            cur_choice, b = new_board()
        else:
            # start with existing board
            cur_choice, b = board_builder()
            # for word in board, eliminate choices from valid_set
            print("processing board")
            for word in b.board:
                print("eliminating words incompatible with {}...".format(word.__str__()))
                cur_choice, valid_set, score = eliminate_choices(valid_set, word)
                print("system suggested {0} [{1:.3g}] out of {2} remaining words as a next word".format( cur_choice, score , len(valid_set)))
            print("I suggest you start with {0} [{1:.3g}].".format(cur_choice, score))
    
    pattern = ask()
    if pattern and b.length<7:
        word = b.add_word(cur_choice, pattern)
        b.list_words()

        # eliminate choices
        next_guess, valid_set, score = eliminate_choices(valid_set, word)

        # suggest next word
        print("{} remaining words to choose from".format(len(valid_set)))
        cur_choice = random.choice(list(valid_set)).upper()
        print("I suggest {0} [{1:.3g}] as your next word".format(next_guess, score))
        loop(valid_set, b, next_guess)
    else:
        b.add_word(cur_choice, "GGGGG") 
        b.list_words()
        return

print("Welcome to the Wordle Solver!")
i = input("Start fresh or build a board? (0, 1):")
if i == "1":
    b=False
else:
    b=True

loop(valid_set, b)