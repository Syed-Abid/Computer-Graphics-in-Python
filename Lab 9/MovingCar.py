import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 626, 407
CAR_WIDTH, CAR_HEIGHT = 100, 100
FPS = 60

# Colors
Light_Blue = (173, 216, 230)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Animation")

# Load the background image
background_image = pygame.image.load("bench.png")  # Replace with your background image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load the car image
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Initial car position
car_x, car_y = WIDTH // 2 - CAR_WIDTH // 2, HEIGHT - CAR_HEIGHT  # Start at the bottom

# Initial background position
#background_x = 0

# Velocity of the car
car_velocity = 1  # Adjust as needed

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car automatically to the right
    car_x += car_velocity

    # Move the background to the left to simulate forward movement
    #background_x -= car_velocity


    # Ensure the car stays within the screen boundaries
    if car_x > WIDTH:
        car_x = -CAR_WIDTH  # Reset the car's position to the left side

    # If the background reaches the end, reset it to its initial position
    #if background_x <= -WIDTH:
    #    background_x = -1

    # Draw the background
    #screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (0, 0))
    # Draw the car at the updated position
    screen.blit(car_image, (car_x, car_y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)