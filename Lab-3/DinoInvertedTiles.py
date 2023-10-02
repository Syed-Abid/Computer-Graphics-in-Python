from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

screenWidth = 650
screenHeight = 450
rotate_x = 0.5

def setWindow(xs, xe, ys, ye):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(int(xs), int(xe), int(ys), int(ye))

def drawPolyLineFile(fileName):
    with open(fileName, 'r') as inStream:
        numpolys = float(inStream.readline().strip())
        for _ in range(int(numpolys)):
            numPoints = float(inStream.readline().strip())
            glBegin(GL_LINE_STRIP)
            for _ in range(int(numPoints)):
                x, y = map(float, inStream.readline().strip().split())
                glVertex2f(x, y)
            glEnd()

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, float(screenWidth), 0.0, float(screenHeight))
    glViewport(0, 0, screenWidth, screenHeight)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(10):
        for j in range(10):
            if (i + j) % 2 == 0:
                setWindow(0, 640, 0, 480)
            else:
                setWindow(0, 640, 480, 0)
            glViewport(i * 64, j * 44, 64, 44)
            drawPolyLineFile("dino.dat")
    glFlush()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Inverted Dinos".decode())
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()
