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
   
    # Set Things Up
    colors = ['blue', 'red', 'orange', 'yellow', 'lime', 'cyan', 'violet', 'purple', 'sea green', 'white']
    turtle.bgcolor('black')
    t = turtle.Pen()
    t.width(15)
    t.up()
    t.left(180)
    t.forward(300)
    t.down()
    t.speed(0)

    # N
    t.pencolor(colors[1])
    t.right(90)
    t.forward(100)
    t.right(135)
    t.forward(140)
    t.left(135)
    t.forward(100)

    # I
    t.pencolor(colors[2])
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
    t.pencolor(colors[3])
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
    t.pencolor(colors[4])
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
    t.pencolor(colors[5])
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
    t.pencolor(colors[6])
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
    t.pencolor(colors[7])
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
    t.up()
    t.forward(30)
    t.right(90)
    t.down()

    # Lines Below Name
    t.pencolor("turquoise")
    t.forward(430)
    t.up()
    t.pencolor("magenta")
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.down()
    t.forward(350)
    t.up()
    t.pencolor("red")
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.down()
    t.forward(270)
    t.up()
    t.pencolor("yellow")
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.down()
    t.forward(190)

    # Balloons
    t.up()
    t.forward(210)
    t.left(90)
    t.up()
    t.forward(220)
    t.pencolor("red")
    t.width(50)
    t.down()
    t.forward(0)
    t.width(10)
    t.up()
    t.backward(27)
    t.down()
    t.pencolor("white")
    t.backward(73)
    t.up()
    t.left(90)
    t.forward(610)
    t.right(90)
    t.forward(100)
    t.width(50)
    t.pencolor("violet")
    t.down()
    t.forward(0)
    t.width(10)
    t.up()
    t.backward(27)
    t.down()
    t.pencolor("blue")
    t.backward(73)
    
# Functions To Run
if __name__ == "__main__":
    drawSquareSpiral()
#    drawCircleSpiral()
#    drawNikhil()
