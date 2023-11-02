import pygame
import math

# Constants
screen_width = 700
screen_height = 650
rotate_x = 0.5

def draw_polyline_file(dino):
    try:
        with open(dino, "r") as in_stream:
            numpolys = int(in_stream.readline())

            for j in range(numpolys):
                num_points = int(in_stream.readline())
                points = []

                for i in range(num_points):
                    x, y = map(float, in_stream.readline().split())
                    points.append((x, y))

                # Draw the polyline
                for i in range(len(points) - 1):
                    pygame.draw.line(screen, (0, 0, 0), points[i], points[i + 1], 2)

    except IOError:
        print("Can't open the file!")

def set_window(xs, xe, ys, ye):
    pygame.display.set_mode((xe, ye))
    pygame.display.set_caption("Dino CircleTiles Drawing")

def my_init():
    pygame.init()
    global screen, clock
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dino CircleTiles Drawing")
    clock = pygame.time.Clock()

def my_display():
    screen.fill((255, 255, 255))

    num_motifs = 12
    center_x = 300
    center_y = 300
    radius = 120
    motif_width = 200
    motif_height = 200

    for i in range(num_motifs):
        angle = 2 * math.pi * i / num_motifs
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))

        draw_polyline_file("dino.dat")

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    set_window(0, screen_width, 0, screen_height)
    my_init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        my_display()

    pygame.quit()
