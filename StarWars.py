import turtle
import random
import time
from random import randint
from random import seed

for _ in range(1):
    value = randint(-300, 300)


def fel():
    ypozicio = urhajo.ycor()
    ypozicio += 20
    urhajo.sety(ypozicio)


def le():
    ypozicio = urhajo.ycor()
    ypozicio -= 20
    urhajo.sety(ypozicio)


def jobbra():
    xpozicio = urhajo.xcor()
    xpozicio += 20
    urhajo.setx(xpozicio)


def balra():
    xpozicio = urhajo.xcor()
    xpozicio -= 20
    urhajo.setx(xpozicio)


kijelzo = turtle.Turtle()
kijelzo.hideturtle()

space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("Background.png")
space.addshape("sprite.gif")
space.addshape("meteor2.gif")
space.tracer(0)
space.listen()
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor_jobbrol = turtle.Turtle()
meteor_jobbrol.shape("meteor2.gif")
meteor_jobbrol.penup()

meteor_jobbrol.setx(400)
meteor_jobbrol.sety(value)

szamlalo = 0

while meteor_jobbrol.xcor() > -400:
    space.update()
    time.sleep(0.1)
    meteor_mozgas = meteor_jobbrol.xcor()
    meteor_mozgas -= 50
    meteor_jobbrol.setx(meteor_mozgas)

while meteor_jobbrol.xcor() <= -400:
    szamlalo += 1
    kijelzo.clear()
    kijelzo.color("white")
    kijelzo.penup()
    kijelzo.goto(0,260) 
    kijelzo.write(f"Pontjaid: {szamlalo}", align="center", font=("Arial", 30, "bold"))
    for _ in range(1):
        value = randint(-300, 300)
    meteor_jobbrol.setx(400)
    meteor_jobbrol.sety(value)
    while meteor_jobbrol.xcor() > -400:
        space.update()
        time.sleep(0.1)
        meteor_mozgas = meteor_jobbrol.xcor()
        meteor_mozgas -= 50
        meteor_jobbrol.setx(meteor_mozgas)

        if urhajo.ycor()>300:
            urhajo.sety(-300)
        if urhajo.xcor()>400:
            urhajo.setx(-400)
        if urhajo.xcor()<-400:
            urhajo.setx(400)
        if urhajo.ycor()<-300:
            urhajo.sety(300)
