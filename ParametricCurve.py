from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Function to draw the rose curve
def drawRoseCurve(k):
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glBegin(GL_LINE_STRIP)
    for angle in range(0, int(2 * math.pi * 100), 1):
        angle /= 100.0
        radius = math.sin(k * angle)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2d(x, y)
    glEnd()

# Display callback function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    glLoadIdentity()

    # Translate to the center of the window
    glTranslatef(0.0, 0.0, 0.0)

    # Scale the curve
    glScalef(0.5, 0.5, 1.0)

    drawRoseCurve(6)  # You can adjust the value of 'k' here

    glFlush()

# Reshape callback function
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 400)
    glutCreateWindow(b"Rose Curve".decode())

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color to white

    glutMainLoop()
    return 0

if __name__ == "__main__":
    main()
