from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Constants for the screen window size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Define the golden ratio
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

def draw_golden_rect(x, y, width, height):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

def draw_regression(x, y, width, height, depth):
    if depth <= 0:
        return

    draw_golden_rect(x, y, width, height)

    new_width = width / GOLDEN_RATIO
    new_height = height / GOLDEN_RATIO
    new_x = x + (width - new_width) / 2
    new_y = y + (height - new_height) / 2

    draw_regression(new_x, new_y, new_width, new_height, depth - 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Set line color to black

    # Calculate the initial dimensions of the largest golden rectangle
    initial_width = min(SCREEN_WIDTH, SCREEN_HEIGHT * GOLDEN_RATIO)
    initial_height = initial_width / GOLDEN_RATIO

    # Center the largest golden rectangle in the screen window
    initial_x = (SCREEN_WIDTH - initial_width) / 2
    initial_y = (SCREEN_HEIGHT - initial_height) / 2

    # Draw the regression of golden rectangles
    draw_regression(initial_x, initial_y, initial_width, initial_height, 10)

    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutCreateWindow(b"Golden Rectangle Regression")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
