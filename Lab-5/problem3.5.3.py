import turtle

def forward(distance):
    turtle.forward(distance)

def left_turn():
    turtle.left(60)

def right_turn():
    turtle.right(60)

def interpret_commands(commands):
    for command in commands:
        if command == 'F':
            forward(50)  # You can adjust the distance as needed
        elif command == 'L':
            left_turn()
        elif command == 'R':
            right_turn()

def main():
    turtle.speed(1)  # Set the drawing speed
    commands = "FLFLFLFRFLFLFLFRFLFLFLFR"
    interpret_commands(commands)
    turtle.done()

if __name__ == "__main__":
    main()
