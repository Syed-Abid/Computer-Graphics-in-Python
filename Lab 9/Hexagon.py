from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

HEX_RADIUS = 0.05  # Radius of the hexagons

def myInit():
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Hexagonal Tiling")
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-0.1, 1, -0.1, 1)

def motif():
    glColor3f(0.5, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for i in range(6):
        angle = 2.0 * math.pi * i / 6
        x = HEX_RADIUS * math.cos(angle)
        y = HEX_RADIUS * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

def pushCT():
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

def popCT():
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def translate2D(dx, dy):
    glMatrixMode(GL_MODELVIEW)
    glTranslated(dx, dy, 0.0)

def tiling():
    pushCT()
    translate2D(0.0, 0.0)
    for row in range(7):
        pushCT()
        for col in range(11):
            motif()
            if col % 2 != 0:
                translate2D(0.075, -0.045)
            else:
                translate2D(0.075, 0.045)
        popCT()
        translate2D(0.0, 0.087)
    popCT()

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    tiling()
    glFlush()

def main():
    glutInit(sys.argv)
    myInit()
    glutDisplayFunc(myDisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()
