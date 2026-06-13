"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01

FIRST_ZIG_X = 100
SECOND_ZIG_X = 200

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    square = canvas.create_rectangle(start_x, start_y, SQUARE_SIZE, start_y + SQUARE_SIZE)
    # zig zag path
    canvas.create_line(start_x, start_y, FIRST_ZIG_X, start_y + FIRST_ZIG_X, 'blue')
    canvas.create_line(FIRST_ZIG_X, start_y + FIRST_ZIG_X, SECOND_ZIG_X, start_y, 'blue')
    canvas.create_line(SECOND_ZIG_X, start_y, CANVAS_WIDTH, start_y + FIRST_ZIG_X, 'blue')
        
    while start_x < CANVAS_WIDTH:
        start_x += VELOCITY # we always move right

        if start_x > FIRST_ZIG_X:
            if start_x > SECOND_ZIG_X:
                # move down
                start_y += VELOCITY
            else:
                # move up
                start_y -= VELOCITY
        else:
            # move down
            start_y += VELOCITY
        
        canvas.moveto(square, start_x, start_y) # this will move the square to start_x, start_y!
        time.sleep(DELAY)
        
        
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()