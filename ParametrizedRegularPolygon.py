from OpenGL.GL import *
from OpenGL.GLUT import *
import math

PI = 3.14159265358979323846

class Point2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

def moveTo(p):
    glVertex2f(p.x, p.y)

def lineTo(p):
    glVertex2f(p.x, p.y)

def ngon(n, cx, cy, radius, rotAngle):
    if n < 3:
        return

    glBegin(GL_LINE_LOOP)

    angle = rotAngle * PI / 180
    angleInc = 2 * PI / n

    startPoint = Point2(cx + radius * math.cos(angle), cy + radius * math.sin(angle))
    moveTo(startPoint)

    for _ in range(n):
        angle += angleInc
        vertex = Point2(cx + radius * math.cos(angle), cy + radius * math.sin(angle))
        lineTo(vertex)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 0.0)  # Set color to black

    sides = 6            # Number of sides in the polygon
    centerX = 0.0        # X-coordinate of the center
    centerY = 0.0        # Y-coordinate of the center
    radius = 0.5         # Radius of the polygon
    rotation = 30.0      # Rotation angle in degrees

    ngon(sides, centerX, centerY, radius, rotation)

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Ngon".decode())
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color to white
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
