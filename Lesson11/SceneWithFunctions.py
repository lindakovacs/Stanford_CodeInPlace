from graphics import Canvas
import math

# TODO: You should define a function like draw_cloud
# for trees, as well as for any extra elements in the scene.

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # 1. Draw three clouds at different locations and colors
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 20, 40, 'pink')
    draw_cloud(canvas, 260, 20, 'purple')

    # 2. Draw three trees with different leaf colors
    draw_tree(canvas, 60, 'green')
    draw_tree(canvas, 130, 'red')
    draw_tree(canvas, 300, 'orange')

def draw_tree(canvas, x, leaf_color):
    """
    Draws a tree where 'x' is the left edge of the tree trunk.
    The bottom of the tree is fixed at TREE_BOTTOM_Y.
    The 'leaf_color' parameter changes the color
    for each specific tree.
    """

    # Calculate trunk coordinates
    trunk_left = x
    trunk_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_right = x + TRUNK_WIDTH
    trunk_bottom = TREE_BOTTOM_Y
    
    # Draw trunk (using a reddish-brown color)
    canvas.create_rectangle(trunk_left, trunk_top, trunk_right, trunk_bottom, 'brown')
    
    # Calculate leaves coordinates (centered horizontally over the trunk)
    trunk_center_x = x + (TRUNK_WIDTH / 2)
    leaves_left = trunk_center_x - (LEAVES_SIZE / 2)
    leaves_top = trunk_top - LEAVES_SIZE
    leaves_right = trunk_center_x + (LEAVES_SIZE / 2)
    leaves_bottom = trunk_top
    
    # Draw leaves using the color passed into the function
    canvas.create_oval(leaves_left, leaves_top, leaves_right, leaves_bottom, leaf_color)

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

if __name__ == '__main__':
    main()