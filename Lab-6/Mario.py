import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
import pygame.mixer
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
LIGHT_BLUE = (173, 216, 230)  # Light blue color
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Game")

# Load Mario's sprites
mario_right_images = [pygame.image.load("E:\CG Python\LAB6\MarioRun1.png"),
                      pygame.image.load("E:\CG Python\LAB6\MarioRun2.png"),
                      pygame.image.load("E:\CG Python\LAB6\MarioRun3.png"),
                      pygame.image.load("E:\CG Python\LAB6\MarioStanding.png")]

# Flip Mario's sprites to face left
mario_left_images = [pygame.transform.flip(img, True, False) for img in mario_right_images]

# Load Mario's jump sprite
mario_jump_image = pygame.image.load("E:\CG Python\LAB6\MarioJump.png")

# Initialize Mario's properties
mario_width, mario_height = mario_right_images[0].get_width(), mario_right_images[0].get_height()
mario_x = 100
mario_y = 400
mario_x_speed = 5
mario_y_speed = 0
gravity = 1

# Create a clock to control frame rate
clock = pygame.time.Clock()

# Create a variable to track Mario's current sprite
current_sprite = 0
is_jumping = False
facing_right = True  # Initially, Mario is facing right

# Load and play background music
background_music = pygame.mixer.Sound("E:\CG Python\LAB6\MarioSong.wav")
background_music.play(-1)  # -1 makes the music loop indefinitely

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move Mario and perform boundary checks
    if keys[pygame.K_LEFT]:
        mario_x -= mario_x_speed
        facing_right = False  # Mario is facing left
        current_sprite = (current_sprite + 1) % 4  # Cycle through Mario's walking sprites
        if mario_x < 0:  # Left boundary check
            mario_x = 0

    if keys[pygame.K_RIGHT]:
        mario_x += mario_x_speed
        facing_right = True  # Mario is facing right
        current_sprite = (current_sprite + 1) % 4  # Cycle through Mario's walking sprites
        if mario_x > WIDTH - mario_width:  # Right boundary check
            mario_x = WIDTH - mario_width

    # Make Mario jump
    if keys[pygame.K_SPACE] and not is_jumping:
        mario_y_speed = -15
        is_jumping = True

    # Apply gravity
    mario_y_speed += gravity
    mario_y += mario_y_speed

    # Collision with the ground
    if mario_y >= HEIGHT - mario_height:  # Bottom boundary check
        mario_y = HEIGHT - mario_height
        is_jumping = False

    # Clear the screen
    screen.fill(LIGHT_BLUE)

    # Blit Mario's sprite based on whether he is jumping or not
    if is_jumping:
        screen.blit(mario_jump_image, (mario_x, mario_y))
    else:
        if facing_right:
            screen.blit(mario_right_images[current_sprite], (mario_x, mario_y))
        else:
            screen.blit(mario_left_images[current_sprite], (mario_x, mario_y))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

# Stop and quit the background music
background_music.stop()

# Quit Pygame
pygame.quit()
sys.exit()
