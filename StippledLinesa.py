from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width = 800
window_height = 600
line_pattern = 0x00FF  # Default pattern
line_factor = 1  # Default factor
points = []

def draw_lines():
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(line_factor, line_pattern)

    glBegin(GL_LINES)
    for i in range(0, len(points), 2):
        glVertex2f(points[i][0], points[i][1])
        glVertex2f(points[i+1][0], points[i+1][1])
    glEnd()

    glDisable(GL_LINE_STIPPLE)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_lines()
    glutSwapBuffers()

def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        points.append((x / window_width, 1 - y / window_height))
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Stippled Lines")

    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)

    while True:
        try:
            pattern_input = input("Enter pattern in hexadecimal notation (e.g., 0xEECC): ")
            line_pattern = int(pattern_input, 16)
            factor_input = int(input("Enter factor value: "))
            line_factor = factor_input
            glutMainLoop()
        except ValueError:
            print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
