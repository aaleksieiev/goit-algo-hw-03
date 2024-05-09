import turtle
import argparse

def koch_curve(turtle, line_length, depth):
    if depth <= 0:
        turtle.forward(line_length)
    else:
        koch_curve(turtle, line_length / 3, depth - 1)
        turtle.left(60)
        koch_curve(turtle, line_length / 3, depth - 1)
        turtle.right(120)
        koch_curve(turtle, line_length / 3, depth - 1)
        turtle.left(60)
        koch_curve(turtle, line_length / 3, depth - 1)

def main():
    parser = argparse.ArgumentParser(description="Koch snowflake")
    parser.add_argument("-d", "--depth", required=False, default=4, help="depth")

    args = parser.parse_args()

    # Set up the window and turtle.
    win = turtle.Screen()
    win.bgcolor("white")

    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)  # Fastest speed.

    # Initial positioning.
    koch_turtle.penup()
    koch_turtle.goto(-300, 200)
    koch_turtle.pendown()

    koch_curve(koch_turtle, 500, args.depth)

    turtle.done()

if __name__ == "__main__":
    main()