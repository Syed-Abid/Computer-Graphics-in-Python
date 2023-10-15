
import turtle

def polyspiral(length, angle, incr, num):
    for _ in range(num):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        length += incr
        turtle.left(angle)

def main():
    turtle.speed(1)  # Set the drawing speed
    length = 50.0   # Initial length of the segment
    angle = 30      # Angle to turn after each segment
    incr = 5.0      # Length increment after each segment
    num = 10        # Number of segments

    polyspiral(length, angle, incr, num)

    turtle.done()

if __name__ == "__main__":
    main()
