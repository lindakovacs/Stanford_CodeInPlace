from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.

    Karel finds the midpoint of Row 1 by placing boundary beepers 
    at both ends and moving them inward until they meet.
    """

    # 1. Setup initial boundaries at (1,1) and the far East wall
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    
    # 2. Prepare to move boundaries inward
    turn_around()
    move()
    
    # 3. Shrink the boundaries until the entire row is filled or they meet
    while no_beepers_present():
        fill_the_line()
        
    # 4. Handle the final beeper placement based on orientation
    if facing_west():
        put_beeper()
    else:
        turn_around()
        move()
        put_beeper()
        
    # 5. Cleanup Phase: Move to the wall to prepare for clearing extra beepers
    while front_is_clear():
        move()
    turn_around()
    
    # 6. Pick up the temporary markers (Caution: Logic may clear all beepers)
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()    
    
    # 7. Final Step: Return to the identified midpoint
    turn_around()
    while no_beepers_present():
        move()
    turn_around()

def fill_the_line():
    """
    Moves until a beeper is found, then steps back one corner 
    to place a new inward boundary beeper.
    """
    while no_beepers_present():
        move()
    turn_around()
    move()
    put_beeper()
    move() # Step away to check for the next inner square
  
def turn_around():
    """Helper to rotate Karel 180 degrees."""
    turn_left()
    turn_left()
        
if __name__ == '__main__':
    main()