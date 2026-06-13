from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP*9) / 10
BRICK_HEIGHT = 10
DELAY = 0.02

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # 1. Setup the Bricks
    bricks = setup_bricks(canvas)
    
    # 3. Setup the Paddle
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, PADDLE_Y + PADDLE_HEIGHT, "black")
    
    # 5. Finishing Touches: Keep track of turns/lives
    lives = 3
    
    while lives > 0 and len(bricks) > 0:
        # 2. Add a Bouncing Ball
        ball = canvas.create_oval(
            CANVAS_WIDTH/2 - BALL_RADIUS, CANVAS_HEIGHT/2 - BALL_RADIUS,
            CANVAS_WIDTH/2 + BALL_RADIUS, CANVAS_HEIGHT/2 + BALL_RADIUS,
            "black"
        )
        
        # Give the ball a random starting trajectory downward
        change_x = random.randint(3, 6)
        if random.random() > 0.5:
            change_x = -change_x
        change_y = 5
        
        # Pause briefly before the serve
        time.sleep(1) 
        
        # Animation loop for a single turn
        while True:
            # --- Move the Paddle ---
            mouse_x = canvas.get_mouse_x()
            # Calculate the new X to keep the mouse in the exact center of the paddle
            paddle_x = mouse_x - (PADDLE_WIDTH / 2)
            
            # Constrain paddle to stay on screen
            if paddle_x < 0:
                paddle_x = 0
            elif paddle_x + PADDLE_WIDTH > CANVAS_WIDTH:
                paddle_x = CANVAS_WIDTH - PADDLE_WIDTH
                
            canvas.moveto(paddle, paddle_x, PADDLE_Y)
            
            # --- Move the Ball ---
            canvas.move(ball, change_x, change_y)
            ball_left = canvas.get_left_x(ball)
            ball_top = canvas.get_top_y(ball)
            ball_right = ball_left + (BALL_RADIUS * 2)
            ball_bottom = ball_top + (BALL_RADIUS * 2)
            
            # --- Wall Collisions ---
            if ball_left <= 0 or ball_right >= CANVAS_WIDTH:
                change_x = -change_x
            if ball_top <= 0:
                change_y = -change_y
                
            # If the ball hits the bottom wall, the player loses a turn
            if ball_bottom >= CANVAS_HEIGHT:
                lives -= 1
                canvas.delete(ball)
                break
                
            # --- 4. Check for Collisions ---
            colliders = canvas.find_overlapping(ball_left, ball_top, ball_right, ball_bottom)
            
            for obj in colliders:
                if obj == ball:
                    continue # The ball can't collide with itself!
                    
                if obj == paddle:
                    # "Glue Bug" Fix: Only bounce the ball UP if it's currently falling DOWN.
                    if change_y > 0:
                        change_y = -change_y
                    break
                else:
                    # It must be a brick! 
                    canvas.delete(obj)
                    bricks.remove(obj)
                    change_y = -change_y
                    break # Only process one collision per frame
                    
            # Check if all bricks are gone
            if len(bricks) == 0:
                canvas.delete(ball)
                break
                
            time.sleep(DELAY)
            
    # --- Game Over Sequence ---
    if len(bricks) == 0:
        canvas.create_text(CANVAS_WIDTH/2 - 70, CANVAS_HEIGHT/2, text="You Win!", font="Arial", font_size=35, color="green")
    else:
        canvas.create_text(CANVAS_WIDTH/2 - 90, CANVAS_HEIGHT/2, text="Game Over!", font="Arial", font_size=35, color="red")

def setup_bricks(canvas):
    """
    Helper function that builds the 10 rows of colored bricks.
    Returns a list containing all the brick object IDs.
    """
    bricks = []
    # Two rows of each color
    colors = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green", "cyan", "cyan"]
    start_y = 60 # Gap from the top of the screen
    
    for row in range(10):
        color = colors[row]
        for col in range(10):
            # Calculate exact coordinate for each brick using the Constants
            x = col * (BRICK_WIDTH + BRICK_GAP)
            y = start_y + row * (BRICK_HEIGHT + BRICK_GAP)
            
            brick = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, color)
            bricks.append(brick)
            
    return bricks

if __name__ == '__main__':
    main()