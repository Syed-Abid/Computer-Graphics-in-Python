import turtle

def forward(distance, width):
    turtle.pensize(width)
    turtle.forward(distance)

def left_turn(angle):
    turtle.left(angle)

def right_turn(angle):
    turtle.right(angle)

def draw_single_motif():
    forward(40, 5)  # Draw the main horizontal line
    left_turn(90)   # Turn left to draw vertical line

    forward(40, 5)  # Draw the vertical line
    right_turn(90)  # Turn right to draw the bottom horizontal line

    forward(40, 5)  # Draw the bottom horizontal line
    right_turn(90)  # Turn right to draw the second vertical line

    forward(40, 5)  # Draw the second vertical line
    left_turn(90)   # Turn left to prepare for the next motif

def draw_meander(num_motifs):
    for _ in range(num_motifs):
        draw_single_motif()

def main():
    turtle.speed(1)  # Set the drawing speed
    num_motifs = 6

    draw_meander(num_motifs)

    turtle.done()

if __name__ == "__main__":
    main()
