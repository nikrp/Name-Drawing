# Imports
import turtle
import random

def drawSquareSpiral():
    t = turtle.Pen()
    for x in range(100):
        t.forward(x)
        t.left(90)

def drawStar():
    t = turtle.Pen()
    for x in range(100):
        t.forward(x)
        t.left(160)
        
def drawCircleSpiral():
    t = turtle.Pen()
    for x in range(100):
        t.forward(x/2)
        t.left(30)

def drawNikhil():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow', 'lime', 'magenta', 'sea green', 'white']
    turtle.bgcolor('black')
    
    # Set Things Up
    t = turtle.Pen()
    t.width(15)
    t.up()
    t.left(180)
    t.forward(300)
    t.down()

    # N
    t.pencolor(random.choice(colors))
    t.right(90)
    t.forward(100)
    t.right(135)
    t.forward(140)
    t.left(135)
    t.forward(100)

    # I
    t.pencolor(random.choice(colors))
    t.up()
    t.right(90)
    t.forward(30)
    t.down()
    t.forward(1)
    t.right(90)
    t.up()
    t.forward(30)
    t.down()
    t.forward(70)

    # K
    t.pencolor(random.choice(colors))
    t.up()
    t.left(90)
    t.forward(30)
    t.left(90)
    t.down()
    t.forward(100)
    t.backward(50)
    t.right(45)
    t.forward(70)
    t.backward(70)
    t.right(90)
    t.forward(70)
    t.left(45)

    # H
    t.pencolor(random.choice(colors))
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)
    t.forward(100)

    # I
    t.pencolor(random.choice(colors))
    t.up()
    t.right(90)
    t.forward(30)
    t.down()
    t.forward(1)
    t.right(90)
    t.up()
    t.forward(30)
    t.down()
    t.forward(70)

    # L
    t.pencolor(random.choice(colors))
    t.left(90)
    t.up()
    t.forward(30)
    t.down()
    t.forward(50)
    t.backward(50)
    t.left(90)
    t.forward(100)
    t.right(90)

    # !
    t.pencolor(random.choice(colors))
    t.up()
    t.forward(80)
    t.down()
    t.right(90)
    t.forward(70)
    t.up()
    t.forward(30)
    t.down()
    t.forward(1)

    # Decorations
       
# Functions to run.
if __name__ == "__main__":
#    drawSquareSpiral()
#    drawCircleSpiral()
    drawNikhil()
