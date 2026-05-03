"""
This is a worked example. It shows an example of Karel
using a while loop to place a row of beepers
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper()
        move()
    # needed because of the fence-post bug
    put_beeper()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()