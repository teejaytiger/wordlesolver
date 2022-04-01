## Wordle Solver

It solves Wordles

This is what it looks like:

![wordle solver in action](https://github.com/teejaytiger/wordlesolver/blob/master/wordlesolve1.PNG "Don't do drugs")

### Installation:
Have python 3.8+ installed

### Running the solver:
Open up your favorite wordle app and in a cmd window, run with:
` python solver.py`

The solver will give you suggestions, including starters, and give you the best next choice for each row. 

> Note: Only does hard mode strategy. Sorryyyyyy

> Other note: I might make more strategies, starting with [VKRS](https://github.com/teejaytiger/wordlesolver/wiki/Performance-VS-VKRS) and modified VKRS, removing the words `QUICK` and `FJORD` and attempting to modify the word set to include `I`, `O`, and `D` while leaving three guesses remaining. 


### Future strategies:

Dumb strategy, removes keyboard options to "catch" more letters (**not valid for hard mode**)
* 5 word starters (waltz, quick, gybes, nymph, fjord - leaves v and x)
* 4 word starters (craft, light, mound, pesky - leaves bjqvwxz out)
* 3 word starters
* 2 word starters

Improved starter word options (**Valid for hard mode**)
* likely win starter list (adept, clamp, plaid, scalp, clasp, depot, print, recap, strap, tramp)
* quick win starter list (slice, tried, crane, leant, close, trice, train, slate, lance, trace)
* top three likely win starters (slice, tried, crane)

Board-aware starter traversal (**not valid for hard mode**)
* Checks the valid word list length and scores and suggest a winner at a sufficient threshold

Turn-Aware strategy/weighting adjustments

Thanks!