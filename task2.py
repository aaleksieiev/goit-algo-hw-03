import turtle

def koch_curve(turtle, line_length, depth):
    if depth <= 0:
        turtle.forward(line_length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, line_length/2, depth-1)
            turtle.right(angle)

def main():
    # Set up the window and turtle.
    win = turtle.Screen()
    win.bgcolor("white")

    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)  # Fastest speed.

    # Initial positioning.
    koch_turtle.penup()
    koch_turtle.goto(-400, 200)
    koch_turtle.pendown()

    koch_curve(koch_turtle, 400, 7)

    turtle.done()

if __name__ == "__main__":
    main()