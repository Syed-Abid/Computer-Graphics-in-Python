import turtle

def turbase(thickness):

    t = turtle.Turtle()
    t.pensize(thickness)
    t.color('lightgray')
    t.penup()    
    t.goto(4,0)
    t.pendown()
    t.right(90)
    t.forward(400)


def turwings(thickness, startingdegree):
    t = turtle.Turtle()
    t.pensize(thickness)
    colors = ['red', 'blue', 'orange', 'green', 'black', 'brown']    
    t.color("darkblue")
    i=30
    
    t.penup()
    t.forward(20)
    t.pendown()
    t.right(startingdegree)
    t.forward(300)
    t.left(174)
    t.forward(300)
    
    
    t.right(45)
    t.forward(300)
    t.left(175)
    t.forward(300)
    
    
    t.right(70)
    t.forward(300)
    t.left(175)
    t.forward(300)
    
    t.fillcolor('red')    
turbase(20)
turwings(3, 257.5)
turtle.done()