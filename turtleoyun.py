import turtle
import random

d_b = turtle.Screen()
d_b.bgcolor("grey")
turt1 = turtle.Turtle()
turt2 = turtle.Turtle()
turt1.hideturtle()
turt1.penup()
turt2.penup()

turt1.setposition(0, 285)
i = 0
turt1.write("Skor: 0", move=False, align="center", font=("Verdana", 15, "normal"))


def turtleP():
    d_b.tracer(0)

    x = random.randint(a=-250, b=250)
    y = random.randint(a=-280, b=280)
    turt2.setposition(x, y)
    turt2.showturtle()
    turt2.shape("turtle")
    turt2.turtlesize(2)
    d_b.tracer(1)
    d_b.delay(500)
    turt2.clear()


def skor(x, y):
    global turt2
    global i
    turt2_pos = turt2.position()
    if abs(x - turt2_pos[0]) <= 50 and abs(y - turt2_pos[1]) <= 50:
        turt1.clear()
        i += 1
        turt1.write("Skor: " + str(i), move=False, align="center", font=("Verdana", 15, "normal"))


while True:
    turtleP()
    turt2.onclick(skor)

d_b.mainloop()
