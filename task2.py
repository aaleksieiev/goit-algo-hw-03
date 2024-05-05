import turtle

def koch_curve(turtle, length_order):
    """
    Draw a Koch snowflake curve.
    :param turtle: Turtle object
    :param length_order: length and order of the curve
    """
    if length_order < 3:
        turtle.forward(length_order)
        return
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, length_order / 3)
            turtle.left(angle)

def main():
    # Set up the window and its attributes
    turtle.setup(width=800, height=600)

    # Create turtle object
    t = turtle.Turtle()

    # Increase the speed of the turtle to the maximum
    t.speed(0)

    # Move the turtle to start position
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # set the order of the Koch curve
    order = 40
    size = 700

    # Draw the Koch Curve
    koch_curve(t, size)

    # Hide the turtle after drawing
    t.hideturtle()

    # Keep the window open
    turtle.mainloop()

if __name__ == "__main__":
    main()