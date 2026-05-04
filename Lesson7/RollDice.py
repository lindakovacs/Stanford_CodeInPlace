"""
File: rolldice.py
------------------
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    
    # Roll die
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Get their total
    total = die1 + die2
    
    # Print out the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()