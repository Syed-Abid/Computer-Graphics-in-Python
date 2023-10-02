from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

screenWidth = 650
screenHeight = 450
rotate_x = 1

def setWindow(xs, xe, ys, ye):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(int(xs), int(xe), int(ys), int(ye))

def keyPress(key, x, y):
    global rotate_x
    
    if key == b'\x1b':
        exit(0)
    if key == GLUT_KEY_UP:
        rotate_x += 0.05
    if key == GLUT_KEY_DOWN:
        rotate_x -= 0.05

    glutPostRedisplay()

def drawPolyLineFile(dino):
    with open(dino, 'r') as inStream:
        numpolys = float(inStream.readline().strip())
        glPushMatrix()
        glScalef(rotate_x, rotate_x, 1.0)
        for _ in range(int(numpolys)):
            numPoints = float(inStream.readline().strip())
            glBegin(GL_LINE_STRIP)
            for _ in range(int(numPoints)):
                x, y = map(float, inStream.readline().strip().split())
                glVertex2f(x, y)
            glEnd()
        glPopMatrix()

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
    drawPolyLineFile("dino.dat")
    glFlush()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Dino Line Drawing".decode())
    glutDisplayFunc(myDisplay)
    glutSpecialFunc(keyPress)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()
