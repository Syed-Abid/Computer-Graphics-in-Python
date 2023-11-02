import turtle
# Create a turtle screen
screen = turtle.Screen()

# Set the window title
screen.title("Robot Graphics")

turtle.bgcolor('skyblue')

def createrectangle(length,breadth,color):
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        if i % 2 != 0:
            turtle.forward(length)
            turtle.right(90)
        else:
            turtle.forward(breadth)
            turtle.right(90)
    turtle.end_fill()
    turtle.penup()

turtle.penup()
turtle.speed(0)

turtle.goto(-100,-150)
createrectangle(20,50,'blue')

turtle.goto(-30,-150)
createrectangle(20,50,'blue')

turtle.goto(-70,-50)
createrectangle(100,15,'gray')

turtle.goto(-25,-50)
createrectangle(100,15,'gray')

turtle.goto(-90,100)
createrectangle(150,100,'red')

turtle.goto(-150,70)
createrectangle(15,60,'gray')

turtle.goto(-150,110)
createrectangle(40,15,'gray')

turtle.goto(10,70)
createrectangle(15,60,'gray')

turtle.goto(55,110)
createrectangle(40,15,'gray')

turtle.goto(-50,120) #neck
createrectangle(20,15,'gray')

turtle.goto(-85,170)
createrectangle(50,90,'red')

turtle.goto(-60,160)
createrectangle(10,40,'white')

turtle.goto(-50,155)
createrectangle(5,5,'black')

turtle.goto(-35,155)
createrectangle(5,5,'black')

turtle.goto(-65,138)
createrectangle(5,50,'yellow')

turtle.goto(-155,130)
createrectangle(25,24,'green')

turtle.goto(-147,130)
createrectangle(15,10,turtle.bgcolor())

turtle.goto(50,130)
createrectangle(25,25,'green')

turtle.goto(58,130)
createrectangle(15,10,turtle.bgcolor())

turtle.hideturtle()
turtle.mainloop()