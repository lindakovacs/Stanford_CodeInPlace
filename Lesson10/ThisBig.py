"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
	# Makes our rectangle centered at (CENTER_X, CENTER_Y)!
    # Since we draw starting at the left-most x and top-most y,
    # we need to take however big our square is (THIS_BIG)
    # and put half of it to the left and above the center, and the other
    # half to the right and below the center.
    canvas.create_rectangle(
		CENTER_X - THIS_BIG / 2,  # Put half of the square to the left of CENTER_X
		CENTER_Y - THIS_BIG / 2,  # Put half of the square above CENTER_Y
		CENTER_X + THIS_BIG / 2,  # Put half of the square to the right of CENTER_X
		CENTER_Y + THIS_BIG / 2   # Put half of the square below CENTER_Y
	)

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()