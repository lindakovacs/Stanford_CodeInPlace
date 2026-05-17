from graphics import Canvas

CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150

# the diameter of the outer red circle
OUTER_DIAMETER = 50

# the left and top coordinates of the outer red circle
OUTER_LEFT_X = (CANVAS_WIDTH - OUTER_DIAMETER)/2
OUTER_TOP_Y = (CANVAS_HEIGHT - OUTER_DIAMETER)/2

# the size of the red band of the ring
# inner_left_x = outer_left_x + RING_WIDTH
RING_WIDTH = 10


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Outer circle
    canvas.create_oval(
        OUTER_LEFT_X, 
        OUTER_TOP_Y,
        OUTER_LEFT_X + OUTER_DIAMETER,
        OUTER_TOP_Y + OUTER_DIAMETER,
        'red'
    )

    # Inner circle
    inner_diameter = OUTER_DIAMETER - 2 * RING_WIDTH
    inner_left_x = OUTER_LEFT_X + RING_WIDTH
    inner_top_y = OUTER_TOP_Y + RING_WIDTH
    canvas.create_oval(
        inner_left_x,
        inner_top_y,
        inner_left_x + inner_diameter,
        inner_top_y + inner_diameter,
        'white'
    )

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
    