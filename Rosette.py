from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

PI = 3.1415926536

class Point2:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def set(self, dx, dy):
        self.x = dx
        self.y = dy

class CP:
    x = 0.0
    y = 0.0

def moveTo(p):
    CP.x = p.x
    CP.y = p.y

def lineTo(p):
    glBegin(GL_LINES)
    glVertex2f(CP.x, CP.y)
    glVertex2f(p.x, p.y)
    glEnd()
    glFlush()
    CP.x = p.x
    CP.y = p.y

def myInit():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1, 0, 0, 0)
    glColor3f(0, 0, 1)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set the orthographic projection

def rosette(N, radius):
    pointlist = []

    theta = (2 * PI) / N
    for c in range(N):
        pointlist.append(Point2(radius * math.sin(theta * c), radius * math.cos(theta * c)))

    for i in range(N):
        for j in range(N):
            moveTo(pointlist[i])
            lineTo(pointlist[j])

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(10, 10, 640, 480)
    rosette(20, 0.66)
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutCreateWindow(b"Rosette".decode())
    glutDisplayFunc(render)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()
