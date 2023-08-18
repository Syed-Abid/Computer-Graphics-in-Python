from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Define the stipple pattern (16x16 pattern)
stipple_pattern = [
    0x0C, 0x1E, 0x3F, 0x7F,
    0xFE, 0xFC, 0xF8, 0xF0,
    0xE0, 0xC0, 0x80, 0x00,
    0x00, 0x01, 0x03, 0x07
]

window_width = 800
window_height = 600
polygon_points = []

def draw_polygon():
    glColor3f(1.0, 0.0, 0.0)  # Red color for the stippled pattern
    glEnable(GL_POLYGON_STIPPLE)
    glPolygonStipple(stipple_pattern)

    glBegin(GL_POLYGON)
    for point in polygon_points:
        glVertex2f(point[0], point[1])
    glEnd()

    glDisable(GL_POLYGON_STIPPLE)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_polygon()
    glutSwapBuffers()

def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        polygon_points.append((x / window_width, 1 - y / window_height))
        glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Stippled Polygon")

    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 1.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)

    glutMainLoop()

if __name__ == "__main__":
    main()
