import turtle

def square(t,x,y,w,color,sidelen):
    """
    t - turtle
    x,y - location
    w - width
    color - color to draw in
    sidelen - length of each side
    return:
        nothing    
    """
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()

    for i in range(4):
        t.forward(50)
        t.right(90)
wn = turtle.Screen()
crush = turtle.Turtle()
square(crush,100,100,5,"blue",4)
squirt = turtle.Turtle()
squirt.penup()
squirt.goto(100,100)
squirt.pendown()
squirt.color("red")
squirt.width(5)
square(squirt)

wn.exitonclick()
wn.mainloop()