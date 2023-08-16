import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

windowWidth = 1600
windowHeight = 900
dot_x = -1
dot_y = -1

VPBottom = 0
VPLeft = 0
VPWidth = 1600
VPHeight = 900

dotsVector = []

def initGL():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)

def drawDot(x, y):
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    for dot in dotsVector:
        drawDot(dot.x, dot.y)
    glFlush()

def reshape(width, height):
    global windowWidth, windowHeight
    windowWidth = width
    windowHeight = height

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, float(windowWidth), 0.0, float(windowHeight))
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboardHandler(key, x, y):
    if key == b'q' or key == b'Q':
        sys.exit(0)
    elif key == b's' or key == b'S':
        pass
    glutPostRedisplay()

def mouseHandler(button, state, x, y):
    global dot_x, dot_y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        dot_x = x
        dot_y = windowHeight - y
        newDot = Dot(x, windowHeight - y)
        dotsVector.append(newDot)
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        glClear(GL_COLOR_BUFFER_BIT)
    glutPostRedisplay()

def motionHandler(x, y):
    global dot_x, dot_y
    dot_x = x
    dot_y = windowHeight - y
    newDot = Dot(x, windowHeight - y)
    dotsVector.append(newDot)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(windowWidth, windowHeight)
    glutCreateWindow(b"Lab 03".decode())
    initGL()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboardHandler)
    glutMouseFunc(mouseHandler)
    glutMotionFunc(motionHandler)
    glutMainLoop()

if __name__ == "__main__":
    main()
