from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move() # Reach the pile at (1, 2)
    
    if beepers_present():
        # 1. Pick up the first beeper to start the process
        pick_beeper()
        
        # 2. As long as there are MORE beepers left in the pile...
        while beepers_present():
            # Move the one Karel is currently holding to the next spot
            move_to_empty_corner()
            put_beeper()
            
            # Return to the pile to get the next one
            return_to_start_pile()
            pick_beeper()
            
        # 3. The very last beeper Karel picked belongs at the start (1, 2)
        put_beeper()
        return_to_begining()


def move_to_empty_corner():
    """
    Moves East until Karel finds a corner that doesn't have a beeper.
    """
    while beepers_present():
        move()

def return_to_start_pile():
    """
    Returns Karel to the second corner (1, 2) where the pile started.
    """
    turn_around()
    # Go all the way back to the West wall
    while front_is_clear():
        move()
    # Turn back around and move one step to reach (1, 2)
    turn_around()
    move()

def turn_around():
    """Helper to turn Karel 180 degrees."""
    turn_left()
    turn_left()

def return_to_begining():
        turn_around()
        move()
        turn_around()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()