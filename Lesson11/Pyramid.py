from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Loop through each row from the bottom up
    for row in range(BRICKS_IN_BASE):
        # Calculate how many bricks belong in this specific row
        bricks_in_row = BRICKS_IN_BASE - row
        
        # Find the starting X coordinate to perfectly center the row horizontally
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) / 2
        
        # Calculate the fixed top and bottom Y coordinates for this entire row
        top_y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT
        bottom_y = CANVAS_HEIGHT - row * BRICK_HEIGHT
        
        # Draw each individual brick side-by-side in the current row
        for brick in range(bricks_in_row):
            left_x = start_x + brick * BRICK_WIDTH
            right_x = left_x + BRICK_WIDTH
            
            # Draw the brick (feel free to change "yellow" to any color you like!)
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "yellow", "black")  

if __name__ == '__main__':
    main()