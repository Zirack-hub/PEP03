import turtle

turtle.title("Cuadrado y Círculo")
turtle.bgcolor("white")
t = turtle.Turtle()
t.color("red")
for _ in range(4):
    t.forward(100)
    t.right(90)
t.penup()
t.goto(150, 0)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()
turtle.done()