import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

screenWidth = 600
screenHeight = 600
rotate_x = 0.5

def drawPolyLineFile(dino):
    try:
        inStream = open(dino, 'r')
    except IOError:
        print("Can't open it!")
        return

    numpolys = float(inStream.readline().strip())
    
    for _ in range(int(numpolys)):
        numPoints = float(inStream.readline().strip())
        glBegin(GL_LINE_STRIP)
        for _ in range(int(numPoints)):
            x, y = map(float, inStream.readline().split())
            glVertex2f(x, y)
        glEnd()

    inStream.close()

def setWindow(xs, xe, ys, ye):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(int(xs), int(xe), int(ys), int(ye))

def myInit():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, float(screenWidth), 0.0, float(screenHeight))
    glViewport(0, 0, screenWidth, screenHeight)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    numMotifs = 12
    centerX = 300
    centerY = 300
    radius = 100
    motifWidth = 200
    motifHeight = 200

    for i in range(numMotifs):
        angle = 2 * math.pi * i / numMotifs
        x = centerX + int(radius * math.cos(angle))
        y = centerY + int(radius * math.sin(angle))

        glViewport(x, y, 64, 44)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        drawPolyLineFile("dino.dat")
        glPopMatrix()  # Add this line to pop the matrix from the stack

    glutSwapBuffers()  # Add this line to swap the buffers and display the content

# Rest of your code remains the same

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Dino CircleTiles Drawing")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()

