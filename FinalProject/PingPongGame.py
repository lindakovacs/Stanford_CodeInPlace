from graphics import Canvas
import time
import random

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
PADDLE_HEAD_SIZE = 50
PADDLE_TOTAL_HEIGHT = 80
BALL_SIZE = 15
PADDLE_SPEED = 20
AI_SPEED = 4

# --- COMPACT UI & SCORE POSITIONS ---
LEFT_BOX_CENTER = 267
RIGHT_BOX_CENTER = 332
SCORE_Y = 15

# --- DRIBBLE-INSPIRED COLOR PALETTE ---
BG_COLOR = "#5D3FBC"      
LEFT_COLOR = "#FFD10D"    
RIGHT_COLOR = "#71D2D2"   
WOOD_COLOR = "#D2D28F"    
BALL_COLOR = "#F7F8DC"    
TEXT_COLOR = "#A7E3D3"    
SHADOW_COLOR = "#454A49"  
BORDER_COLOR = "#FFFFFF"  
UI_LABEL_BG = "#DCE4EE"   
PAGE_FOLD_COLOR = "#D3D3D3"  

# --- HELPER FUNCTIONS ---
def update_paddle(canvas, paddle_parts, direction, speed):
    """Moves paddles, allowing them to go all the way up to the border."""
    current_y = canvas.get_top_y(paddle_parts[0]) 
    
    if direction == 'up' and current_y > 10:
        for part in paddle_parts:
            canvas.move(part, 0, -speed)
    elif direction == 'down' and (current_y + PADDLE_TOTAL_HEIGHT < CANVAS_HEIGHT - 10):
        for part in paddle_parts:
            canvas.move(part, 0, speed)

def create_racket(canvas, x, y, head_color):
    shadow_handle = canvas.create_rectangle(x + 19, y + 44, x + 35, y + PADDLE_TOTAL_HEIGHT + 4, SHADOW_COLOR)
    shadow_head = canvas.create_oval(x + 4, y + 4, x + PADDLE_HEAD_SIZE + 4, y + PADDLE_HEAD_SIZE + 4, SHADOW_COLOR)
    handle = canvas.create_rectangle(x + 15, y + 40, x + 31, y + PADDLE_TOTAL_HEIGHT, WOOD_COLOR)
    head = canvas.create_oval(x, y, x + PADDLE_HEAD_SIZE, y + PADDLE_HEAD_SIZE, head_color)
    return [head, handle, shadow_head, shadow_handle]

def create_explosion(canvas, x, y, direction):
    particles = []
    for _ in range(15):
        spark = canvas.create_oval(x, y, x + 5, y + 5, LEFT_COLOR if direction == 1 else RIGHT_COLOR)
        dx = random.randint(2, 10) * direction
        dy = random.randint(-5, 5)
        particles.append((spark, dx, dy))
        
    for _ in range(20):
        for spark, dx, dy in particles:
            canvas.move(spark, dx, dy)
        time.sleep(0.02)
        
    for spark, dx, dy in particles:
        canvas.delete(spark)

def draw_retro_ui(canvas):
    """Draws the retro name boxes with the flip-page calendar backgrounds in the center."""
    # Main background strip 
    canvas.create_rectangle(140, 10, 460, 50, "#000000")
    
    # Left Label Box (Computer)
    canvas.create_rectangle(140, 10, 240, 50, UI_LABEL_BG)
    canvas.create_text(145, 18, text="COMPUTER", font='Arial', font_size=15, color="#000000")
    
    # Left Score Box (Flip Page Base)
    canvas.create_rectangle(240, 10, 295, 50, BALL_COLOR)
    canvas.create_line(240, 30, 295, 30, PAGE_FOLD_COLOR) 
    
    # Center Divider
    canvas.create_rectangle(295, 10, 305, 50, "#888888")
    
    # Right Score Box (Flip Page Base)
    canvas.create_rectangle(305, 10, 360, 50, BALL_COLOR)
    canvas.create_line(305, 30, 360, 30, PAGE_FOLD_COLOR) 
    
    # Right Label Box (Player)
    canvas.create_rectangle(360, 10, 460, 50, UI_LABEL_BG)
    canvas.create_text(380, 18, text="PLAYER", font='Arial', font_size=16, color="#000000")

def animate_score_flip(canvas, text_obj, new_score, box_x):
    """Animates the optical illusion of the white pages flipping."""
    box_left = box_x - 27
    box_right = box_x + 28
    box_top = 10
    box_bottom = 50
    box_center = 30
    
    top_strips = []
    for i in range(0, 20, 5):
        top_y = box_top + i
        bottom_y = min(top_y + 6, box_center) 
        strip = canvas.create_rectangle(box_left, top_y, box_right, bottom_y, BALL_COLOR)
        top_strips.append(strip)
        time.sleep(0.015) 

    bottom_strips = []
    for i in range(0, 20, 5):
        top_y = box_center + i
        bottom_y = min(top_y + 6, box_bottom)
        strip = canvas.create_rectangle(box_left, top_y, box_right, bottom_y, BALL_COLOR)
        bottom_strips.append(strip)

    canvas.change_text(text_obj, str(new_score))

    for strip in top_strips:
        canvas.delete(strip)

    for strip in bottom_strips:
        canvas.delete(strip)
        time.sleep(0.015)
        
    # Redraw the fold line so it stays crisp on top of the new number
    canvas.create_line(box_left, box_center, box_right, box_center, PAGE_FOLD_COLOR)

def play_confetti(canvas):
    """Generates a falling confetti animation with various shapes upon set completion."""
    colors = [LEFT_COLOR, RIGHT_COLOR, TEXT_COLOR, BALL_COLOR]
    shape_types = ["square", "circle", "triangle"]
    confetti_pieces = []
    
    for _ in range(100):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(-200, 0)
        size = random.randint(6, 16)  
        color = random.choice(colors)
        shape_type = random.choice(shape_types)
        
        # Draw the chosen shape
        if shape_type == "square":
            piece = canvas.create_rectangle(x, y, x + size, y + size, color)
        elif shape_type == "circle":
            piece = canvas.create_oval(x, y, x + size, y + size, color)
        elif shape_type == "triangle":
            piece = canvas.create_polygon(x, y + size, x + size, y + size, x + (size / 2), y, color=color)
            
        dx = random.randint(-2, 2)
        dy = random.randint(3, 8)
        confetti_pieces.append((piece, dx, dy))
        
    # Animate the pieces falling
    for _ in range(100):
        for piece, dx, dy in confetti_pieces:
            canvas.move(piece, dx, dy)
        time.sleep(0.02)

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # 1. Background and Borders
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, BG_COLOR)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, 10, BORDER_COLOR)
    canvas.create_rectangle(0, CANVAS_HEIGHT - 10, CANVAS_WIDTH, CANVAS_HEIGHT, BORDER_COLOR)
    canvas.create_rectangle(0, 0, 10, CANVAS_HEIGHT, BORDER_COLOR)
    canvas.create_rectangle(CANVAS_WIDTH - 10, 0, CANVAS_WIDTH, CANVAS_HEIGHT, BORDER_COLOR)
    
    # 2. Dashed Net
    for y in range(10, CANVAS_HEIGHT, 40):
        canvas.create_rectangle(CANVAS_WIDTH/2 - 2, y, CANVAS_WIDTH/2 + 2, y + 20, TEXT_COLOR)

    # 3. Compact Retro UI Banner with Flip Pages built in
    draw_retro_ui(canvas)
    
    left_score = 0
    right_score = 0
    
    left_score_text = canvas.create_text(LEFT_BOX_CENTER - 10, SCORE_Y, text=str(left_score), font='Arial', font_size=28, color=BG_COLOR)
    right_score_text = canvas.create_text(RIGHT_BOX_CENTER - 10, SCORE_Y, text=str(right_score), font='Arial', font_size=28, color=BG_COLOR)

    # 4. Rackets and Ball 
    left_paddle = create_racket(canvas, 20, CANVAS_HEIGHT/2 - PADDLE_TOTAL_HEIGHT/2, LEFT_COLOR)
    right_paddle = create_racket(canvas, CANVAS_WIDTH - 20 - PADDLE_HEAD_SIZE, CANVAS_HEIGHT/2 - PADDLE_TOTAL_HEIGHT/2, RIGHT_COLOR)
    
    ball_shadow = canvas.create_oval(CANVAS_WIDTH/2 - BALL_SIZE/2 + 4, CANVAS_HEIGHT/2 - BALL_SIZE/2 + 4,
                                     CANVAS_WIDTH/2 + BALL_SIZE/2 + 4, CANVAS_HEIGHT/2 + BALL_SIZE/2 + 4, SHADOW_COLOR)
    ball = canvas.create_oval(CANVAS_WIDTH/2 - BALL_SIZE/2, CANVAS_HEIGHT/2 - BALL_SIZE/2,
                              CANVAS_WIDTH/2 + BALL_SIZE/2, CANVAS_HEIGHT/2 + BALL_SIZE/2, BALL_COLOR)
                              
    ball_dx = 5
    ball_dy = 5
    last_mouse_y = canvas.get_mouse_y()
    
    while True:
        keys = canvas.get_new_key_presses()
        for key in keys:
            if key in ['ArrowUp', 'Up', 'up', 'w', 'W']:
                update_paddle(canvas, right_paddle, 'up', PADDLE_SPEED)
            elif key in ['ArrowDown', 'Down', 'down', 's', 'S']:
                update_paddle(canvas, right_paddle, 'down', PADDLE_SPEED)
                
        current_mouse_y = canvas.get_mouse_y()
        if current_mouse_y != last_mouse_y:
            new_y = current_mouse_y - (PADDLE_TOTAL_HEIGHT / 2)
            
            if new_y < 10:
                new_y = 10
            elif new_y + PADDLE_TOTAL_HEIGHT > CANVAS_HEIGHT - 10:
                new_y = CANVAS_HEIGHT - 10 - PADDLE_TOTAL_HEIGHT
                
            current_y = canvas.get_top_y(right_paddle[0])
            dy = new_y - current_y
            
            for part in right_paddle:
                canvas.move(part, 0, dy)
            last_mouse_y = current_mouse_y
                
        canvas.move(ball, ball_dx, ball_dy)
        canvas.move(ball_shadow, ball_dx, ball_dy) 
        
        ball_left = canvas.get_left_x(ball)
        ball_top = canvas.get_top_y(ball)
        ball_right = ball_left + BALL_SIZE
        ball_bottom = ball_top + BALL_SIZE
        
        left_paddle_top = canvas.get_top_y(left_paddle[0])
        left_paddle_center_y = left_paddle_top + (PADDLE_TOTAL_HEIGHT / 2)
        ball_center_y = ball_top + (BALL_SIZE / 2)
        
        if left_paddle_center_y < ball_center_y - 10:
            update_paddle(canvas, left_paddle, 'down', AI_SPEED)
        elif left_paddle_center_y > ball_center_y + 10:
            update_paddle(canvas, left_paddle, 'up', AI_SPEED)
            
        if ball_top <= 10 or ball_bottom >= CANVAS_HEIGHT - 10:
            ball_dy *= -1 
            
        overlapping_items = canvas.find_overlapping(ball_left, ball_top, ball_right, ball_bottom)
        hit_left = any(part in overlapping_items for part in left_paddle)
        hit_right = any(part in overlapping_items for part in right_paddle)
        if hit_left or hit_right:
            ball_dx *= -1
            
        scored = False
        if ball_left <= 0:
            right_score += 1
            scored = True
            scorer = "right"
            explosion_x = 0
            explosion_y = ball_top
            explosion_dir = 1 
            
        elif ball_right >= CANVAS_WIDTH:
            left_score += 1
            scored = True
            scorer = "left"
            explosion_x = CANVAS_WIDTH
            explosion_y = ball_top
            explosion_dir = -1 
            
        if scored:
            create_explosion(canvas, explosion_x, explosion_y, explosion_dir)

            if (left_score >= 6 and (left_score - right_score >= 2)) or left_score == 7:
                animate_score_flip(canvas, left_score_text, left_score, LEFT_BOX_CENTER)
                canvas.create_text(CANVAS_WIDTH/2 - 200, CANVAS_HEIGHT/2 - 40, text="Computer Wins 🏆 the Set!", font='Arial', font_size=30, color=LEFT_COLOR)
                canvas.create_text(CANVAS_WIDTH/2 - 80, CANVAS_HEIGHT/2 + 10, text="Game Over!", font='Arial', font_size=30, color=TEXT_COLOR)
                play_confetti(canvas)
                break 
                
            elif (right_score >= 6 and (right_score - left_score >= 2)) or right_score == 7:
                animate_score_flip(canvas, right_score_text, right_score, RIGHT_BOX_CENTER)
                canvas.create_text(CANVAS_WIDTH/2 - 150, CANVAS_HEIGHT/2 - 40, text="You Win 🏆 the Set!", font='Arial', font_size=30, color=RIGHT_COLOR)
                canvas.create_text(CANVAS_WIDTH/2 - 80, CANVAS_HEIGHT/2 + 10, text="Game Over!", font='Arial', font_size=30, color=TEXT_COLOR)
                play_confetti(canvas)
                break 
                
            if scorer == "left":
                animate_score_flip(canvas, left_score_text, left_score, LEFT_BOX_CENTER)
            else:
                animate_score_flip(canvas, right_score_text, right_score, RIGHT_BOX_CENTER)
            
            canvas.moveto(ball, CANVAS_WIDTH/2 - BALL_SIZE/2, CANVAS_HEIGHT/2 - BALL_SIZE/2) 
            canvas.moveto(ball_shadow, CANVAS_WIDTH/2 - BALL_SIZE/2 + 4, CANVAS_HEIGHT/2 - BALL_SIZE/2 + 4) 
            ball_dx *= -1 
            time.sleep(0.2) 
            
        time.sleep(0.02)

if __name__ == '__main__':
    main()