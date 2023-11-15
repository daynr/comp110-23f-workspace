"""Create a scene with a person sitting in a dorm room doing homework."""

__author__ = "730690615"

from turtle import Turtle, done


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float, color: str) -> None:
    """Draw a filled rectangle with the given dimensions and top-left corner at (x, y)."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor(color)
    a_turtle.begin_fill()
    for _ in range(2):
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)
    a_turtle.end_fill()


def draw_person(a_turtle: Turtle, x: float, y: float, body_color: str) -> None:
    """Draw a more realistic person sitting on a chair at coordinates (x, y)."""
    # Draw the body
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor(body_color)
    a_turtle.begin_fill()
    a_turtle.setheading(90)
    a_turtle.circle(30, 180)
    a_turtle.forward(60)
    a_turtle.circle(30, 180)
    a_turtle.forward(60)
    a_turtle.end_fill()

    # Draw the head
    a_turtle.penup()
    a_turtle.goto(x, y + 60)
    a_turtle.pendown()
    a_turtle.fillcolor("peachpuff")
    a_turtle.begin_fill()
    a_turtle.circle(20)
    a_turtle.end_fill()

    # Draw the legs
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("blue")
    a_turtle.begin_fill()
    a_turtle.setheading(270)
    a_turtle.forward(20)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.right(90)
    a_turtle.forward(20)
    a_turtle.right(90)
    a_turtle.forward(20)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.end_fill()


def draw_desk(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a detailed desk at the given coordinates (x, y)."""
    # Draw the desk surface
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("saddlebrown")
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(180)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.left(90)
    a_turtle.forward(180)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.end_fill()

    # Draw desk legs
    for i in range(2):
        a_turtle.penup()
        a_turtle.goto(x + 20 + i * 140, y - 20)
        a_turtle.pendown()
        a_turtle.fillcolor("saddlebrown")
        a_turtle.begin_fill()
        a_turtle.setheading(0)
        a_turtle.forward(20)
        a_turtle.left(90)
        a_turtle.forward(20)
        a_turtle.left(90)
        a_turtle.forward(20)
        a_turtle.left(90)
        a_turtle.forward(20)
        a_turtle.end_fill()


def draw_chair(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a detailed chair at the given coordinates (x, y)."""
    # Draw the chair seat
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("gray")
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(60)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.left(90)
    a_turtle.forward(60)
    a_turtle.left(90)
    a_turtle.forward(20)
    a_turtle.end_fill()

    # Draw chair backrest
    a_turtle.penup()
    a_turtle.goto(x + 60, y)
    a_turtle.pendown()
    a_turtle.fillcolor("gray")
    a_turtle.begin_fill()
    a_turtle.setheading(90)
    a_turtle.forward(30)
    a_turtle.right(90)
    a_turtle.forward(20)
    a_turtle.right(90)
    a_turtle.forward(30)
    a_turtle.right(90)
    a_turtle.forward(20)
    a_turtle.end_fill()


def draw_poster(a_turtle: Turtle, x: float, y: float, text: str) -> None:
    """Draw a poster on the wall at the given coordinates (x, y) with the specified text."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    # Calculate the width of the poster based on the text length and padding
    poster_width = len(text) * 10 + 20

    a_turtle.fillcolor("lightblue")
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(poster_width)
    a_turtle.left(90)
    a_turtle.forward(60)
    a_turtle.left(90)
    a_turtle.forward(poster_width)
    a_turtle.left(90)
    a_turtle.forward(60)
    a_turtle.end_fill()

    # Write the text on the poster
    a_turtle.penup()
    a_turtle.goto(x + 10, y + 10)
    a_turtle.pendown()
    a_turtle.color("black")
    a_turtle.write(text, align="left", font=("Arial", 12, "normal"))

    # Hide the turtle arrow
    a_turtle.hideturtle()


def draw_dorm_layout(a_turtle: Turtle) -> None:
    """Draw the layout of the dorm room including walls, window, and door."""
    a_turtle.speed(0)
    a_turtle.pensize(3)

    # Draw walls
    draw_rectangle(a_turtle, -200, -200, 400, 200, "lightgray")

    # Draw window
    draw_rectangle(a_turtle, -120, 40, 60, 60, "lightblue")

    # Draw door
    draw_rectangle(a_turtle, 20, -200, 60, 100, "saddlebrown")


def draw_potted_plant(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a potted plant at the given coordinates (x, y)."""
    # Hide the turtle arrow
    a_turtle.hideturtle()

    # Draw pot
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("saddlebrown")
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.circle(20, 180)
    a_turtle.forward(40)
    a_turtle.circle(20, 180)
    a_turtle.forward(40)
    a_turtle.end_fill()

    # Draw leaves
    a_turtle.penup()
    a_turtle.goto(x, y + 40)
    a_turtle.pendown()
    a_turtle.fillcolor("green")
    a_turtle.begin_fill()
    a_turtle.setheading(90)
    a_turtle.circle(20, 180)
    a_turtle.end_fill()


def draw_foliage() -> None:
    """Draw potted plants on both sides of the room."""
    ertle = Turtle()
    ertle.speed(0)
    ertle.penup()

    for x in [-160, 100]:
        draw_potted_plant(ertle, x, -200)

    done()


def draw_scene() -> None:
    """Draw the entire dorm room scene with a person, desk, chair, posters, and foliage."""
    ertle = Turtle()
    ertle.speed(0)  # Fastest drawing speed

    # Draw the dorm room layout
    draw_dorm_layout(ertle)

    # Draw the desk, chair, and person
    draw_desk(ertle, -75, -70)
    draw_chair(ertle, -135, -70)
    draw_person(ertle, -135, -15, "lightblue")

    # Draw posters on the wall
    draw_poster(ertle, -90, 40, "UNC!")
    draw_poster(ertle, 20, 40, "GDTBATH!")

    # Draw potted plants
    draw_foliage()

    done()


if __name__ == "__main__":
    draw_scene()
