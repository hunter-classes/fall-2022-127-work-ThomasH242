import turtle

def hexagon(t, sides, x, y, color, w, sidelen):
    t.penup()
    t.goto(x, y)
    t.width(w)
    t.color(color)
    t.pendown()
    for i in range(sides):
        t.forward(sidelen)
        t.right(360 / sides)
def square(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    for i in range(4):
        t.forward(50)
        t.right(90)
def triangle(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    for i in range(3):
        t.forward(sidelen)
        t.right(120)
wn = turtle.Screen()
S = turtle.Turtle()
hexagon(S, 9, 150, 150, "blue", 5, 50)
wn.exitonclick()
wn.mainloop()
