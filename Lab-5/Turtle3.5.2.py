from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

screenWidth = 640
screenHeight = 440

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
        glColor3f(1.0, 1.0, 1.0)
        glLineWidth(5.0)
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
    # 3.5.2 (Example Motif)
    # for part(a) set i < 1, for part(b) set i < 4
    for i in range(4):
        cvs.forward(3 * L, 1)
        cvs.turn(90)
        cvs.forward(L, 1)
        cvs.turn(90)
        cvs.forward(L, 1)
        cvs.turn(90)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Example 3.5.2")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight)
    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(display)

    glutMainLoop()

if __name__ == "__main__":
    main()
