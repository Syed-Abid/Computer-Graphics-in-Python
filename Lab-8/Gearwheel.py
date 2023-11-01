import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gearwheel Animation")

# Load gearwheel images
gearwheel_images = []
for i in range(4):
    gearwheel_images.append(pygame.image.load(f'gearwheel{i}.png'))

# Set up variables for animation
angle = 0
image_index = 0
image = gearwheel_images[image_index]
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rotate the gearwheel
    angle += 2  # You can adjust the rotation speed here
    if angle >= 360:
        angle = 0

    # Switch gearwheel images to create animation
    image_index = int(angle / 90)
    image = gearwheel_images[image_index]

    # Rotate the image
    rotated_image = pygame.transform.rotate(image, angle)

    # Update the display
    screen.fill(BLACK)
    screen.blit(rotated_image, rotated_image.get_rect(center=image_rect.center))
    pygame.display.flip()

    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
