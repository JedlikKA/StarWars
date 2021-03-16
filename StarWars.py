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
space.addshape("meteor1.gif")
space.tracer(0)
space.listen()
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor = turtle.Turtle()
meteor.penup()
shapes = ["meteor2.gif","meteor1.gif"]
meteor.shape(random.choice(shapes))
meteor.setx(400)
meteor.sety(random.randint(-270,270))


pontok = 0
elet = 0
pen=turtle.Turtle()
pen.hideturtle()


while True:

    space.update()
    time.sleep(0.1)

    if urhajo.ycor() > 300:
        urhajo.sety(-300)
    if urhajo.ycor() < -300:
        urhajo.sety(300)
    if urhajo.xcor() > 400:
        urhajo.setx(-400)
    if urhajo.xcor() < -400:
        urhajo.setx(400)

    if meteor.xcor() < -400 or meteor.ycor() < -300 or meteor.ycor() > 300:
        meteor.shape(random.choice(shapes))
        meteor.setx(400)
        meteor.sety(random.randint(-270,270))

        pontok += 1
        pen.clear()
        pen.color("white")
        pen.penup()
        pen.goto(-320,260) 
        pen.write(f"Pontjaid: {pontok}", align="center", font=("Arial", 20, "bold"))


    if urhajo.distance(meteor.xcor(), meteor.ycor()) < 70:
        meteor.shape(random.choice(shapes))
        meteor.setx(400)
        meteor.sety(random.randint(-270,270))
        
        elet += 1 
        pen.clear()
        pen.color("red")
        pen.penup()
        pen.goto(0,260) 
        pen.write(f"Találat: {elet}", align="center", font=("Arial",20,"bold"))



    if meteor.shape() == "meteor2.gif":
        meteor.setx(meteor.xcor()-15)
    elif meteor.shape() == "meteor1.gif":
        meteor.setx(meteor.xcor()-15)
    else:
        meteor.setx(meteor.xcor()+15)
    
    if elet == 3:
        space.clear()                                                                  
        kijelzo.write("MEGHALTÁL!", align="center", font=("Arial", 30, "bold"))
