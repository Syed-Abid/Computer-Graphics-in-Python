from OpenGL.GL import *
from OpenGL.GLUT import *

RED = 1
GREEN = 2
BLUE = 3
WHITE = 4

angle = 0.0
red = 1.0
blue = 1.0
green = 1.0

def renderScene():
    global angle, red, green, blue
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angle, 0.0, 1.0, 0.0)
    glColor3f(red, green, blue)

    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()

    angle += 1.0
    glutSwapBuffers()

def processMenuEvents(option):
    global red, green, blue
    if option == RED:
        red = 1.0
        green = 0.0
        blue = 0.0
    elif option == GREEN:
        red = 0.0
        green = 1.0
        blue = 0.0
    elif option == BLUE:
        red = 0.0
        green = 0.0
        blue = 1.0
    elif option == WHITE:
        red = 1.0
        green = 1.0
        blue = 1.0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(320, 320)
    glutCreateWindow(b"Menu Test".decode())
    glutDisplayFunc(renderScene)
    glutIdleFunc(renderScene)
    
    glutCreateMenu(processMenuEvents)
    glutAddMenuEntry(b"Red".decode(), RED)
    glutAddMenuEntry(b"Green".decode(), GREEN)
    glutAddMenuEntry(b"Blue".decode(), BLUE)
    glutAddMenuEntry(b"White".decode(), WHITE)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
