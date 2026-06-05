from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    # Passed canvas, x, and y to the function
    draw_car(canvas, x, y)

    x = 100
    y = 100
    # Passed canvas, x, and y to the function
    draw_car(canvas, x, y)

# Added parameters to accept canvas, x, and y
def draw_car(canvas, x, y):
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()