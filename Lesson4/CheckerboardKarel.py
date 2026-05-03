from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.

    Karel creates a checkerboard by alternating between rows 
    that start with a beeper and rows that start with a gap.
    """

    put_beeper()
    
    # Draw every row except the last one.
    # The condition 'left_is_clear' ensures we don't try to jump past the top wall.
    while left_is_clear():
        draw_row()
        jump_row() 
        
    # Draw the final row at the top of the world.
    draw_row()
    
    # Final requirement: Karel returns to the starting position (bottom-left).
    return_to_starting_point()
    
def draw_row():
    """
    Moves across a single row, placing beepers on every other corner.
    Includes safety checks for narrow worlds (like 3x1).
    """
    while front_is_clear():
        # Check if front is clear before every move to prevent crashing in small worlds.
        if front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()    
        
def jump_row():
    """
    Transitions Karel from the end of one row to the start of the next,
    ensuring the checkerboard pattern remains offset.
    """
    # Return to the West wall of the current row.
    turn_around()
    while front_is_clear():
        move()
        
    # Check if Row 1 started with a beeper to determine Row 2's starting position.
    if beepers_present():
        # If the start has a beeper, move up and offset one step to the right.
        turn_right()
        move()
        turn_right()
        # Safety check for narrow worlds where moving forward might hit a wall.
        if front_is_clear():
            move()
            put_beeper()
    else:
        # If the start is empty, move up and place a beeper immediately.
        turn_right()
        move()
        turn_right()
        put_beeper()
    
def return_to_starting_point():
    """
    Navigates Karel back to the bottom-left corner (1, 1) facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

# --- Helper Functions ---
def turn_around():
    """Rotates Karel 180 degrees."""
    turn_left()
    turn_left()
 
def turn_right():
    """Rotates Karel 90 degrees to the right."""
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()