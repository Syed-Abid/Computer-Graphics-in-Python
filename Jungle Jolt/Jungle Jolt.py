import sys
import pygame
from pygame.locals import *
import pickle
from pygame import mixer
from os import path

#initializing the setup
pygame.mixer.pre_init(44100, -16 , 2, 512)
mixer.init()
pygame.init()

clock = pygame.time.Clock()
fps = 60

#Setting up the screen
screen_width = 1000
screen_height = 700

#defne font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

#level variable
max_levels = 7
level = 0

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Jungle Jolt')
if path.exists(f'E:\CG Python\TwodGame\level{level}_data'):
    pickle_in = open(f'E:\CG Python\TwodGame\level{level}_data','rb')
    world_data = pickle.load(pickle_in)
#world_data = [
#[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
#[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
#[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
#[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
#[1, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
#[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#]


#game variables
tile_size = 50  # Original tile size
game_over = 0
main_menu = True
score = 0
col_thresh = 20
#level = 1

#define colors
white = (255,255,255)
blue = (0,0,255)

# Calculate the scale factor
width_scale = screen_width / (len(world_data[0]) * tile_size)
height_scale = screen_height / (len(world_data) * tile_size)
scale_factor = min(width_scale, height_scale)

# Scale the tile_size and adjust the screen size
tile_size *= scale_factor
screen_width = len(world_data[0]) * tile_size
screen_height = len(world_data) * tile_size

# Set up the screen with the adjusted size
screen = pygame.display.set_mode((int(screen_width), int(screen_height)))


#load images
sun_img = pygame.image.load('E:\CG Python\TwodGame\img\sun.png')
bg_img = pygame.image.load('E:\CG Python\TwodGame\img\sky.png')
restart_img = pygame.image.load('E:\CG Python\TwodGame\img\destart_btn.png')
start_img = pygame.image.load('E:\CG Python\TwodGame\img\start_btn.png')
exit_img = pygame.image.load('E:\CG Python\TwodGame\img\exit_btn.png')

#load sounds
pygame.mixer.music.load('E:\CG Python\TwodGame\img\music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('E:\CG Python\TwodGame\img\coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('E:\CG Python\TwodGame\img\jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('E:\CG Python\TwodGame\img\scream.mp3')
game_over_fx.set_volume(0.5)


def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


def reset_level(level):
    player.reset(100, screen_height - 130)
    dlob_group.empty()
    lava_group.empty()
    exit_group.empty()
    if path.exists(f'E:\CG Python\TwodGame\level{level}_data'):
        pickle_in = open(f'E:\CG Python\TwodGame\level{level}_data','rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world


class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def draw(self):
        action = False
        #get mouse positions
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        #draw button
        screen.blit(self.image,self.rect)

        return action
    

class Player():
    def __init__(self,x,y):
        self.reset(x,y)

    def update(self,game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5

        if game_over == 0:
        #get key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False: #and self.in_air == False
                jump_fx.play()
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1 :
                    self.image = self.images_left[self.index]
            
            #handle animation
            if self.counter > walk_cooldown: 
                self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1 :
                self.image = self.images_left[self.index]

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            #self.in_air = True
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx,self.rect.y,self.width,self.height):
                    dx = 0
                
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height):
                    #check if below the ground i.e: jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0 
                    #check if above the ground i.e: falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0 
                        #self.in_air = False

            #check for collision with enemies
            if pygame.sprite.spritecollide(self,dlob_group,False):
                game_over = -1
                game_over_fx.play()

            #check for collision with lava
            if pygame.sprite.spritecollide(self,lava_group,False):
                game_over = -1
                game_over_fx.play()

            #check for collision with exit
            if pygame.sprite.spritecollide(self,exit_group,False):
                game_over = 1

            #check for collisions in platform
            for platform in platform_group:
                #collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if platform below
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    #check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top -1
                        dy = 0
                        self.in_air = False
                        dy = 0
                    #move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction


            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.image = self.dead_image
            draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5
        
        #draw player onto the screen
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen,(255,255,255),self.rect,2)    

        return game_over
    
    def reset(self,x,y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1,5):
            img_right = pygame.image.load(f'E:\CG Python\TwodGame\img\guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40 , 80))
            img_left = pygame.transform.flip(img_right,True,False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('E:\CG Python\TwodGame\img\ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        #self.in_air = True

class World():
    def __init__(self, data):
        self.tile_list = []

        # Load images
        dirt_img = pygame.image.load('E:\CG Python\TwodGame\img\dirt.png')
        grass_img = pygame.image.load('E:\CG Python\TwodGame\img\grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (int(tile_size), int(tile_size)))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (int(tile_size), int(tile_size)))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    dlob= Enemy(col_count * tile_size, row_count * tile_size)
                    dlob_group.add(dlob)
                if tile == 4:
                    platform = Platform(col_count * tile_size, row_count * tile_size,1 , 0)
                    platform_group.add(platform)
                if tile == 5:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    platform_group.add(platform)
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                col_count += 1
            row_count += 1

    def draw(self):
     for tile in self.tile_list:
        screen.blit(tile[0], tile[1])
        #pygame.draw.rect(screen,(255,255,255),tile[1],2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('E:\CG Python\TwodGame\img\dlob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('E:\CG Python\TwodGame\img\platform.png')
        self.image = pygame.transform.scale(img,(tile_size , tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1



class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('E:\CG Python\TwodGame\img\lava.png')
        self.image = pygame.transform.scale(img,(tile_size , tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('E:\CG Python\TwodGame\img\coin.png')
        self.image = pygame.transform.scale(img,(tile_size // 2 , tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('E:\CG Python\TwodGame\img\exit.png')
        self.image = pygame.transform.scale(img,(tile_size , int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player(100, screen_height - 130)
dlob_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

#create dummy coin for showing the score
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin) 

#load in level data and create world
#pickle_in = open(f'E:\CG Python\TwodGame\level{level}_data','rb')
#world_data = pickle.load(pickle_in)
world = World(world_data)

#create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 300, screen_height // 2 + 100, start_img)
exit_button = Button(screen_width // 2 + 50, screen_height // 2 + 100, exit_img)


run = True
while run:
    
    clock.tick(fps)
    screen.blit(bg_img,(0,0))
    screen.blit(sun_img,(100,100))
	
    if main_menu == True:
        if exit_button.draw():
            pygame.quit()
            sys.exit()
        if start_button.draw():
            main_menu = False
    else:
        world.draw()
        
        if game_over == 0:
            dlob_group.update()
            platform_group.update()
            #update score
            #check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X' + str(score), font_score, white, tile_size - 10, 10)

        dlob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)
        
        game_over = player.update(game_over)

        #if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        #if player has completed the level
        if game_over == 1:
            #reset game and goto next level
            level += 1
            if level <= max_levels:
                #reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0
            else:
                draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                #restart game
                if restart_button.draw():
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()


