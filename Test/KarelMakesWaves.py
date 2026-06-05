from karel.stanfordkarel import *

def main():
    # Loop 4 times to draw 4 waves
    for i in range(4):
        make_wave()
        # Move forward twice to step over the gap and into the start of the next wave
        if front_is_clear():
            move()
            move()

def make_wave():
    """
    Draws a single wave (a triangle of 3 beepers) and returns 
    Karel to the bottom row, facing East.
    """
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()

    # Turn around and go back down to the ground
    turn_left()
    turn_left()
    move()

    # Face East again, ready for the next move
    turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()