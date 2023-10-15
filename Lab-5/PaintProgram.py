"You can draw circle and traingle with t and c keys"
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class Shape:
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        glBegin(GL_TRIANGLES)
        glVertex2f(150, 50)
        glVertex2f(100, 150)
        glVertex2f(200, 150)
        glEnd()

class Circle(Shape):
    def draw(self):
        PI = 3.14159
        segments = 50
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(320, 240)
        for i in range(segments + 1):
            angle = 2.0 * PI * i / segments
            x = 50 * math.cos(angle)
            y = 50 * math.sin(angle)
            glVertex2f(x + 320, y + 240)
        glEnd()

screenWidth = 640
screenHeight = 480
shapes = []
currentShape = None

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for shape in shapes:
        shape.draw()

    glFlush()

def myKeys(key, x, y):
    global currentShape
    if key == b't':
        currentShape = Triangle()
        shapes.append(currentShape)
        glutPostRedisplay()
    elif key == b'c':
        currentShape = Circle()
        shapes.append(currentShape)
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Simple Drawing Program")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)
    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(display)
    glutKeyboardFunc(myKeys)

    glutMainLoop()

    for shape in shapes:
        del shape

if __name__ == "__main__":
    main()
