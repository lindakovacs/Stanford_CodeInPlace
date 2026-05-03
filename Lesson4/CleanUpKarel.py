"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: This starter code is a solution, but it's messy! Try decomposing it. If you need help, try looking at some of the comments for ideas on what to decompose.
"""

from karel.stanfordkarel import *

def main():
    # If we aren't at the top row (we use a while loop because we don't know how many rows there are)
    while left_is_clear():
        clean_row()  # Pick up a row of beepers 
        return_to_first_column()  # Move back to the first column
        move_up()  # Move up to the next row
        turn_right()  # Reset Karel for loop pre-conditions by turning right to face East 
    
    ### Pick up the final row of beepers ###
    clean_row()
            
def turn_right():
    # Makes Karel turn right
    for i in range(3):
        turn_left()
        
def turn_around():
    # Makes Karel turn around
    for i in range(2):
        turn_left()

def safe_pick_beeper():
    """
    Makes Karel check for a beeper, picking it up if there is one present.
    Pre: None.
    Post: No beepers will be on the square Karel is on.
    """
    if beepers_present():
        pick_beeper()

def move_to_wall():
    """
    Makes Karel move to the next wall in the direction that it's facing.
    Pre: None.
    Post: Karel is facing the same direction as before and is now at a wall.
    """
    while front_is_clear():  # We don't know where the next wall is, so use a while-loop to move until we find one
        move()

def move_up():
    """
    Makes Karel move up a row.
    Pre: Karel is facing West and has no wall above it.
    Post: Karel is facing North and is one row higher than where it started.
    """
    turn_right()
    move()

def clean_row():
    """
    Karel cleans up an entire row of beepers.
    Pre: Karel is facing a direction to travel across a row.
    Post: Karel is on the opposite side of the world from where it started.
    """
    while front_is_clear():
        safe_pick_beeper()
        move()
    
    # Pick final column's beeper if present (fence-post bug)
    safe_pick_beeper()

def return_to_first_column():
    """
    Returns Karel to the first column.
    Pre: Karel is facing East.
    Post: Karel is facing West and is in column one.
    """
    turn_around()
    move_to_wall()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()