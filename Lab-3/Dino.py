import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

screenWidth = 650
screenHeight = 450

def drawPolyLineFile(dino):
    with open('dino.dat', 'r') as inStream:
        numpolys = int(inStream.readline().strip())
        for j in range(numpolys):
            numPoints = int(inStream.readline().strip())
            glBegin(GL_LINE_STRIP)
            for i in range(numPoints):
                x, y = map(float, inStream.readline().split())
                glVertex2f(x, y)
            glEnd()
    
    glFlush()

def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)
    glViewport(0, 0, screenWidth, screenHeight)

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    drawPolyLineFile("dino.dat")
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Dino Line Drawing")
    glutDisplayFunc(myDisplay)
    myInit()
    glutMainLoop()

if __name__ == "__main__":
    main()
