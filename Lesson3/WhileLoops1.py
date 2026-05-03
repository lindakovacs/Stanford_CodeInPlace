"""
This is a worked example. It shows a simple while loop 
that makes Karel move to the end of the wall, no matter
how long the world is!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()