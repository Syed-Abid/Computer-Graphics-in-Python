import pygame
from pygame.locals import *
from OpenGL.GL import *
import math

# Initialize Pygame
pygame.init()

# Create a Pygame window
screenWidth = 800
screenHeight = 600
pygame.display.set_mode((screenWidth, screenHeight), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Motifs drawing")

# Function to initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-80.0, 80.0, -80.0, 80.0, -1.0, 1.0)
    glViewport(20, 20, 580, 580)

# Function to draw the flake motif
def flakeMotif():
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 5.0)
    glVertex2f(20.0, 5.0)
    glVertex2f(30.0, 25.0)
    glVertex2f(35.0, 18.0)
    glVertex2f(25.0, 5.0)
    glVertex2f(30.0, 5.0)
    glVertex2f(45.0, 15.0)
    glVertex2f(50.0, 13.0)
    glVertex2f(35.0, 5.0)
    glVertex2f(55.0, 5.0)
    glVertex2f(60.0, 0.0)
    glEnd()

# Function to draw the snowflake
def drawFlake():
    for i in range(6):
        flakeMotif()
        glScalef(1.0, -1.0, 1.0)
        flakeMotif()
        glScalef(1.0, -1.0, 1.0)
        glRotatef(60.0, 0.0, 0.0, 1.0)

# Function to draw the star motif
def starmotif():
    glBegin(GL_LINE_STRIP)
    glVertex2f(3.0, 3.0)
    glVertex2f(0.0, 8.0)
    glVertex2f(-3.0, 0.0)
    glVertex2f(-2.0, -1.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(2.0, 3.0)
    glVertex2f(3.0, 3.0)
    glEnd()

# Function to draw the star
def drawStar():
    for i in range(5):
        starmotif()
        glRotatef(72.0, 0.0, 0.0, 1.0)

# Function to display
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    init()
    drawFlake()
    glFlush()
    pygame.display.flip()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display()
