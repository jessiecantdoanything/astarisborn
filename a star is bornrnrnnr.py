import turtle
turtle.shape("turtle")
turtle.color("Slate Gray")

turtle.speed(0.4)

def star(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

def starSpiral():
    for i in range(300):
        star(i*3)
        turtle.right(4)



starSpiral()
