from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

class Canvas:
    def __init__(self, width, height, windowTitle):
        self.width = width
        self.height = height
        self.windowTitle = windowTitle

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(20, 20)
        
        self.window = glutCreateWindow(windowTitle)
        glutDisplayFunc(self.display)  # Register the display callback
        self.initGL()

    def initGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Set clear color to black

    def setWindow(self, left, right, bottom, top):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(left, right, bottom, top)
        glMatrixMode(GL_MODELVIEW)

    def setViewport(self, left, right, bottom, top):
        glViewport(left, bottom, right - left, top - bottom)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # Red color
        glVertex2f(0.0, 0.5)
        glColor3f(0.0, 1.0, 0.0)  # Green color
        glVertex2f(-0.5, -0.5)
        glColor3f(0.0, 0.0, 1.0)  # Blue color
        glVertex2f(0.5, -0.5)
        glEnd()
        
        glFlush()

def main():
    canvas = Canvas(800, 600, "Canvas Title")
    glutMainLoop()

if __name__ == "__main__":
    main()
