import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Maze Generation and Solving")
screen.bgcolor("white")

# Set the dimensions of the maze
ROWS = 20
COLS = 30
CELL_SIZE = 20

# Create a maze grid with walls
maze = [['wall' for _ in range(COLS)] for _ in range(ROWS)]

# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-COLS * CELL_SIZE / 2, ROWS * CELL_SIZE / 2)
turtle.pendown()

# Generate the maze using recursive backtracking
def generate_maze(row, col):
    maze[row][col] = 'empty'
    directions = ['up', 'down', 'left', 'right']
    random.shuffle(directions)

    for direction in directions:
        if direction == 'up' and row > 1 and maze[row - 2][col] == 'wall':
            maze[row - 1][col] = 'empty'
            generate_maze(row - 2, col)
        elif direction == 'down' and row < ROWS - 2 and maze[row + 2][col] == 'wall':
            maze[row + 1][col] = 'empty'
            generate_maze(row + 2, col)
        elif direction == 'left' and col > 1 and maze[row][col - 2] == 'wall':
            maze[row][col - 1] = 'empty'
            generate_maze(row, col - 2)
        elif direction == 'right' and col < COLS - 2 and maze[row][col + 2] == 'wall':
            maze[row][col + 1] = 'empty'
            generate_maze(row, col + 2)

generate_maze(1, 1)

# Draw the maze
def draw_maze():
    for row in maze:
        for cell in row:
            if cell == 'wall':
                turtle.begin_fill()
                for i in range(4):
                    turtle.forward(CELL_SIZE)
                    turtle.right(90)
                turtle.end_fill()
            turtle.forward(CELL_SIZE)
        turtle.backward(COLS * CELL_SIZE)
        turtle.right(90)
        turtle.forward(CELL_SIZE)
        turtle.left(90)

draw_maze()

# Solve the maze using depth-first search
def solve_maze(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or maze[row][col] == 'visited':
        return False
    if row == ROWS - 2 and col == COLS - 2:
        return True

    maze[row][col] = 'visited'

    if solve_maze(row + 1, col) or solve_maze(row - 1, col) or solve_maze(row, col + 1) or solve_maze(row, col - 1):
        turtle.dot(CELL_SIZE // 3, "green")
        return True

    return False

# Reset the turtle and solve the maze
turtle.penup()
turtle.goto(-COLS * CELL_SIZE / 2 + CELL_SIZE / 2, ROWS * CELL_SIZE / 2 - CELL_SIZE / 2)
turtle.pendown()
turtle.color("red")
turtle.width(2)
turtle.speed(1)

solve_maze(1, 1)

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()
