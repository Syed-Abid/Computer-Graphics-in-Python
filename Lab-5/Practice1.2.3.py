from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

screenWidth = 640
screenHeight = 480

class Canvas:
    def __init__(self):
        self.x = 225
        self.y = 200
        self.angle = 0.0

    def turnTo(self, angle):
        self.angle = angle

    def turn(self, angle):
        self.angle += angle

    def lineTo(self, x, y):
        t_x, t_y = x, y
        glColor3f(1.0, 0.0, 0.0)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        glVertex2f(self.x, self.y)
        glVertex2f(x, y)
        glEnd()
        glFlush()
        self.moveTo(t_x, t_y)

    def moveTo(self, x, y):
        self.x = x
        self.y = y

    def forward(self, dist, isVisible):
        RadPerDeg = 0.017453393
        x = self.x + dist * math.cos(RadPerDeg * self.angle)
        y = self.y + dist * math.sin(RadPerDeg * self.angle)
        if isVisible >= 1:
            self.lineTo(x, y)
        else:
            self.moveTo(x, y)

L = 50.0
cvs = Canvas()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # 3.5.1 Drawing Turtles Figure
    # part (c)
    """L = 200.0
    cvs.forward(L, 1)
    cvs.turn(120)
    cvs.forward(L / 2, 1)
    cvs.turn(120)
    cvs.forward(L / 2, 1)
    cvs.turn(240)
    cvs.forward(L / 2, 1)
    cvs.turn(240)
    cvs.forward(L / 2, 1)
    cvs.turn(120)
    cvs.forward(L / 2, 1)
    cvs.turn(120)
    cvs.forward(L, 1)"""

    # 3.5.2 Drawing a well-known logo
    """L = 100.0
    cvs.forward(L, 1)
    cvs.turn(320)
    cvs.forward(L, 1)
    cvs.turn(220)
    cvs.forward(L, 1)
    cvs.turn(320)
    cvs.forward(L, 1)
    cvs.turn(40)
    cvs.forward(L, 1)
    cvs.turn(40)
    cvs.forward(L, 1)
    cvs.turn(140)
    cvs.forward(L, 1)
    cvs.turn(40)
    cvs.forward(L * 2, 1)

    cvs.turn(90)
    cvs.forward(L, 1)
    cvs.turn(100)
    cvs.forward(L, 1)
    cvs.turn(80)
    cvs.forward(L, 1)"""

    # 3.5.3 Driving the turtle with strings
    input_str = "FLFLFLFRFLFLFLFRFLFLFLFR"
    for key in input_str:
        if key == 'F':
            cvs.forward(30, 1)
        elif key == 'L':
            cvs.turn(60)
        elif key == 'R':
            cvs.turn(-60)

    glFlush()

# 3.5.3 Driving the turtle with strings
def myKeys(key, x, y):
    L = 30
    if key == b'f':
        cvs.forward(L, 1)
    elif key == b'l':
        cvs.turn(60)
    elif key == b'r':
        cvs.turn(-60)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Practice Exercise 3.5.1-3.5.3")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)
    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(display)
    glutKeyboardFunc(myKeys)

    glutMainLoop()

if __name__ == "__main__":
    main()
