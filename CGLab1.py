from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

screenWidth = 640
screenHeight = 480

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(3.9, 3.9, 3.9)  # background color
    glColor3f(12, 12, 13)      # Foreground
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(30, 30)
    glutCreateWindow(b"Lab 1")
    
    glutDisplayFunc(myDisplay)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
