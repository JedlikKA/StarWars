import turtle
import random
import time

def fel():
    ypozizcio= urhajo.ycor()
    ypozizcio += 10
    urhajo.sety(ypozizcio)


def le():
    ypozizcio= urhajo.ycor()
    ypozizcio -= 10
    urhajo.sety(ypozizcio)


def jobbra():
    xpozizcio= urhajo.xcor()
    xpozizcio += 10
    urhajo.setx(xpozizcio)


def balra():
    xpozizcio= urhajo.xcor()
    xpozizcio -= 10
    urhajo.setx(xpozizcio)

space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("Background.png")
space.addshape("sprite.gif")
space.addshape("meteor2.gif")
space.tracer(0)
space.listen()
space.onkeypress(balra,"Left")
space.onkeypress(jobbra,"Right")
space.onkeypress(fel,"Up")
space.onkeypress(le,"Down")


urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteorjobb = turtle.Turtle()
meteorjobb.shape("meteor2.gif")
meteorjobb.penup()

x = random.randint(130, 380)
y = random.randint(-280, 280)
meteorjobb.goto(x, y)
while meteorjobb.xcor()>-400:
    space.update()
    time.sleep(0.2)
    meteormozgas = meteorjobb.xcor()
    meteormozgas -= 10
    meteorjobb.setx(meteormozgas)

while True:

    space.update()
    time.sleep(0.2)

    if urhajo.ycor()>300:
        urhajo.sety(-300)
    if urhajo.xcor()>400:
        urhajo.setx(-400)
    if urhajo.xcor()<-400:
        urhajo.setx(400)
    if urhajo.ycor()<-300:
        urhajo.sety(300)
