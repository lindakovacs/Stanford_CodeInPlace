from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # --- Milestone #1: Set up the World ---
    # Create the blue player square at the top left corner (0,0)
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "blue")
    
    # Create the red goal square at a location that is a multiple of 20
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, "red")
    
    # At the start, the player should be traveling to the right
    dx = SIZE
    dy = 0
    
    # Animation loop
    while True:
        # --- Milestone #3: Handle Key Press ---
        key = canvas.get_last_key_press()
        
        # Update directions based on arrow keys
        # We also check that the snake doesn't reverse direction directly into itself
        if key == 'ArrowLeft' and dx == 0:
            dx = -SIZE
            dy = 0
        elif key == 'ArrowRight' and dx == 0:
            dx = SIZE
            dy = 0
        elif key == 'ArrowUp' and dy == 0:
            dx = 0
            dy = -SIZE
        elif key == 'ArrowDown' and dy == 0:
            dx = 0
            dy = SIZE
            
        # --- Milestone #2: Animate ---
        canvas.move(player, dx, dy)
        
        # Get current coordinates of player and goal
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        
        # --- Milestone #4: Detecting collisions ---
        # Check if the player goes out of bounds
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            print("Game Over!")
            # Optional: Display Game Over on the canvas
            canvas.create_text(CANVAS_WIDTH/2 - 70, CANVAS_HEIGHT/2 - 20, text="Game Over!", font='Arial', font_size=30, color='black')
            break
            
        # --- Milestone #5: Moving the goal ---
        # Check if the player touches the goal
        if player_x == goal_x and player_y == goal_y:
            # We calculate the max grid value by dividing the canvas by 20 and subtracting 1
            max_grid_x = (CANVAS_WIDTH // SIZE) - 1
            max_grid_y = (CANVAS_HEIGHT // SIZE) - 1
            
            # Generate a random multiple of 20 (SIZE)
            new_goal_x = random.randint(0, max_grid_x) * SIZE
            new_goal_y = random.randint(0, max_grid_y) * SIZE
            
            # Move the goal to the new random coordinates
            canvas.moveto(goal, new_goal_x, new_goal_y)
            
        time.sleep(DELAY)        

if __name__ == '__main__':
    main()