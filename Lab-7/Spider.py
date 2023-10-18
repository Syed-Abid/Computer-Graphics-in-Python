import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SPIDER_SIZE = 80
SPIDER_SPEED = 7
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spider Shooting Game")

# Load spider image
spider_image = pygame.image.load("E:\CG Python\Spider Lab\spider1.png")
spider_image = pygame.transform.scale(spider_image, (SPIDER_SIZE, SPIDER_SIZE))

# Load shooting sound
shooting_sound = pygame.mixer.Sound("E:\CG Python\Spider Lab\shoot.wav")

# Load background music
pygame.mixer.music.load("E:\CG Python\Spider Lab\Music.wav")
pygame.mixer.music.play(-1)  # Play background music in a loop

# Create spider sprite
class Spider(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spider_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = SPIDER_SPEED
        self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()

    def move_smoothly(self):
        self.rect.move_ip(self.speed * self.direction.x, self.speed * self.direction.y)
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            # If spider hits the screen edge, change direction
            self.direction = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()

# Create spider sprite group
spider_group = pygame.sprite.Group()
spider = Spider()
spider_group.add(spider)

# Initialize fonts
font = pygame.font.Font(None, 36)

# Game variables
game_over = False

# Game loop
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Play shooting sound
            shooting_sound.play()
            # Check if the click hit the spider
            if spider.rect.collidepoint(event.pos):
                game_over = True

    # Move spider smoothly
    spider.move_smoothly()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the spider sprite
    spider_group.draw(screen)

    # Check if game is over
    if game_over:
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
