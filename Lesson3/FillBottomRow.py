"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
     """ Fills entire bottom row of any sized world with beepers. """
    
    while front_is_clear():
    # We don't know how large the world is, so we can use a while-loop to move until we reach the last column
        put_beeper()
        move()
    # Fencepost problem! We need to put a beeper here or else we will move without placing a beeper on the first square.
    put_beeper()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()