#160, -43, 270, -97, -43, 200, -940, 17, -86 angles
import turtle

wn = turtle.Screen()

Duck = turtle.Turtle()

for steps in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    Duck.left(steps)
    Duck.forward(100)

wn.exitonclick()
#
