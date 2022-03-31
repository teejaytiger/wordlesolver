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


> Note: It doesn't solve hellowordl well due to their distinct inability to adhere to the ruleset. For example, you guess:

> ` L A T E R (E is green)`

> ` S I Z E S `

> In sizes, if the first S is green, and there are no more instances of S, the second S should appear yellow, to indicate that yes, there is an S, but it is not in the right place. Hellowordle will make it blank and confuse the solver. So where hellowordle gives you
` gxxgx`, you should adjust and input 
`  gxxgy` to get the correct solution set. 

Thanks!