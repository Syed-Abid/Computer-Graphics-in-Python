import turtle

# Define custom functions for the drawing commands
def forward(distance, width):
    turtle.pensize(width)
    turtle.forward(distance)

def turn(angle):
    turtle.left(angle)

def draw_motif(L):
    forward(3 * L, 1)
    turn(90)
    forward(L, 1)
    turn(90)
    forward(L, 1)
    turn(90)
    forward(L, 1)
    turn(90)

def main():
    turtle.speed(1)  # Set the drawing speed
    L = 100  # Adjust the length parameter
    draw_motif(L)
    turtle.done()

if __name__ == "__main__":
    main()
