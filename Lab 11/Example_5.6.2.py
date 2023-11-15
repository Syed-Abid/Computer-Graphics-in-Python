from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def axis(len):
    glPushMatrix()
    glBegin(GL_LINES)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 0, len)
    glEnd()

    glTranslated(0, 0, len - 0.2)
    glutWireCone(0.04, 0.2, 12, 9)
    glPopMatrix()

def pushCT():
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

def popCT():
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3d(0, 0, 0)

    axis(0.5)  # x-axis

    glPushMatrix()
    glRotated(90, 0, 1, 0)
    axis(0.5)  # y-axis
    glPopMatrix()

    glPushMatrix()
    glRotated(-90, 1, 0, 0)
    axis(0.5)  # z-axis
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.5, 0.5, 0.5)  # WIRED BIG CUBE
    glutWireCube(1.0)
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.0, 1.0, 0.0)  # WIRED SPHERE
    glutWireSphere(0.25, 10, 8)
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.0, 0.0, 1.0)  # WIRED CONE
    glutWireCone(0.2, 0.25, 10, 8)
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.0, 1.0, 1.0)  # WIRED TEAPOT
    glutWireTeapot(0.2)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.0, 1.0, 0.0)  # WIRED TORUS
    glRotated(90.0, 1, 0, 0)
    glutWireTorus(0.1, 0.3, 10, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslated(1.0, 0.0, 0.0)  # WIRED DODECAHERDON
    glScaled(0.15, 0.15, 0.15)
    glutWireDodecahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.0, 1.0, 1.0)  # WIRED SMALL CUBE
    glutWireCube(0.25)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.0, 0.0, 1.0)  # WIRED SMALL CUBE
    qobj = gluNewQuadric()
    gluQuadricDrawStyle(qobj, GLU_LINE)
    gluCylinder(qobj, 0.2, 0.2, 0.4, 8, 8)
    glPopMatrix()

    glFlush()

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2.0 * (64 / 48.0), 2.0 * (64 / 48.0), -2.0, 2.0, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Transformation Test - Wireframes")

    myInit()
    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == "__main__":
    main()
