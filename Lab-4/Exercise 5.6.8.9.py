from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

screenWidth = 740
screenHeight = 480

class Canvas:
    def __init__(self):
        self.x = 150
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

increment = 3
cvs = Canvas()

def PolySpiral(dist):
    if dist > 200:
        return
    cvs.forward(dist, 1)
    cvs.turn(-144)
    dist += increment
    PolySpiral(dist + increment)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    L = 70.0
    for i in range(3):
        cvs.forward(L, 1)
        cvs.turn(90)
        cvs.forward(L - 20, 1)
        cvs.turn(90)
        cvs.forward(L / 2, 1)
        cvs.turn(270)
        cvs.forward(L / 2, 1)
        cvs.turn(270)
        cvs.forward(L - 20, 1)
        cvs.turn(270)
        cvs.forward(15, 1)
        cvs.turn(90)
        cvs.forward(25, 1)
        cvs.turn(90)
        cvs.forward(15, 1)
        cvs.turn(270)
        cvs.forward(L - 20, 1)
        cvs.turn(270)
        cvs.forward(L / 2, 1)
        cvs.turn(270)
        cvs.forward(L / 2, 1)
        cvs.turn(90)
        cvs.forward(L - 20, 1)
        cvs.turn(90)
        cvs.forward(L, 1)

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Week 5 | 3.5.5 - 3.5.9")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)
    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == "__main__":
    main()
