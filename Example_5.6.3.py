from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# wall function
def wall(thickness):
    glPushMatrix()
    glTranslated(0.5, 0.5 * thickness, 0.5)
    glScaled(1.0, thickness, 1.0)
    glutSolidCube(1.0)
    glPopMatrix()

# tableLeg function
def tableLeg(thick, length):
    glPushMatrix()
    glTranslated(0, length/2, 0)
    glScaled(thick, length, thick)
    glutSolidCube(1.0)
    glPopMatrix()

# jackPart function
def jackPart():
    glPushMatrix()
    glScaled(0.2, 0.2, 1.0)
    glutSolidSphere(1, 15, 15)
    glPopMatrix()
    glPushMatrix()
    glTranslated(0, 0, 1.2)
    glutSolidSphere(0.2, 15, 15)
    glTranslated(0, 0, -2.4)
    glutSolidSphere(0.2, 15, 15)
    glPopMatrix()

# jack function
def jack():
    glPushMatrix()
    jackPart()
    glRotated(90.0, 0, 1, 0)
    jackPart()
    glRotated(90.0, 1, 0, 0)
    jackPart()
    glPopMatrix()

# table function
def table(topWidth, topThickness, legThickness, legLength):
    glPushMatrix()
    glTranslated(0, legLength, 0)
    glScaled(topWidth, topThickness, topWidth)
    glutSolidCube(1.0)
    glPopMatrix()
    dist = 0.95 * topWidth/2.0 - legThickness / 2.0
    glPushMatrix()
    glTranslated(dist, 0, dist)
    tableLeg(legThickness, legLength)
    glTranslated(0, 0, -2 * dist)
    tableLeg(legThickness, legLength)
    glTranslated(-2 * dist, 0, 2*dist)
    tableLeg(legThickness, legLength)
    glTranslated(0, 0, -2*dist)
    tableLeg(legThickness, legLength)
    glPopMatrix()

# displaySolid function
def displaySolid():
    mat_ambient = [0.7, 0.7, 0.7, 1.0]
    mat_diffuse = [0.6, 0.6, 0.6, 1.0]
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = [50.0]

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    lightIntensity = [0.7, 0.7, 0.7, 1.0]
    light_position = [2.0, 6.0, 3.0, 0.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightIntensity)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    winHt = 1.0
    glOrtho(-winHt*64/48.0, winHt*64/48.0, -winHt, winHt, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(2.3, 1.3, 2, 0, 0.25, 0, 0.0, 1.0, 0.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glTranslated(0.4, 0.4, 0.6)
    glRotated(45, 0, 0, 1)
    glScaled(0.08, 0.08, 0.08)
    jack()
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.6, 0.38, 0.5)
    glRotated(30, 0, 1, 0)
    glutSolidTeapot(0.08)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.25, 0.42, 0.35)
    glutSolidSphere(0.1, 15, 15)
    glPopMatrix()

    glPushMatrix()
    glTranslated(0.4, 0, 0.4)
    table(0.6, 0.02, 0.02, 0.3)
    glPopMatrix()

    wall(0.02)

    glPushMatrix()
    glRotated(90.0, 0.0, 0.0, 1.0)
    wall(0.02)
    glPopMatrix()

    glPushMatrix()
    glRotated(-90.0, 1.0, 0.0, 0.0)
    wall(0.02)
    glPopMatrix()

    glFlush()

# main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("shaded example - 3D scene")
    glutDisplayFunc(displaySolid)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glViewport(0, 0, 640, 480)
    glutMainLoop()

if __name__ == "__main__":
    main()
