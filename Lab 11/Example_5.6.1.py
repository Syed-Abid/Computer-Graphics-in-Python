import numpy as np
import math as m
import pygame, sys, random
pygame.init()

#print("\n"*20+"-"*11,"start of program","-"*11)
#Start of math construct
#defining constants
PI = m.pi
WIDTH , HEIGHT = 700, 700
fov = 45 * PI/180
player_pos = np.array([0,0,-4], dtype=np.float32)    # <-- dtype=np.float32
#camera_rot_y = PI/180 * float(input("what's the horizontal angle (degrees)?:"))
#camera_rot_x = PI/180 * float(input("what's the vertical angle (degrees)?:"))
camera_rot_y = 0
camera_rot_x = 0
camera_rot_z = 0

#initialising the player variables.
player_pos = np.array([0,0,-5])
#camera_rot_y = PI/180 * float(input("what's the horizontal angle (degrees)?:"))
#camera_rot_x = PI/180 * float(input("what's the vertical angle (degrees)?:"))
#camera_rot_z = 0

#defining math functions
def a(x,y): # it's to put (0,0) at the center of the screen
    ''' (num,num) -> (num,num)
    takes a coordinates in cartesian and output the number in shitty 
    coordinates png style
    '''
    return(x + WIDTH/2,HEIGHT/2 - y)

def b(array):
    ''' (array or list) -> list
    takes an arrray corresponding to a coordinates in cartesian
    | output the coordinate in array form in png style'''
    return(a(array[0],array[1]))

def Rx(rot_x):  #The rotation matrix over the x axis
    z   = np.matrix([
    [ 1, 0, 0, 0],
    [ 0, m.cos(rot_x), m.sin(rot_x), 0],
    [ 0, -m.sin(rot_x), m.cos(rot_x), 0],
    [ 0, 0, 0, 1 ]
    ])
    return(z)

def Ry(rot_y):#The rotation matrix over the y axis
    z = np.matrix([
    [ m.cos(rot_y), 0,m.sin(rot_y), 0],
    [ 0, 1, 0, 0],
    [ -m.sin(rot_y), 0, m.cos(rot_y), 0],
    [ 0, 0, 0, 1 ],
    ])
    return(z)

def Rz(rot_z): #The rotation matrix over the z axis
    z = np.matrix([
    [ m.cos(rot_z), m.sin(rot_z), 0, 0],
    [- m.sin(rot_z), m.cos(rot_z), 0, 0],
    [ 0, 0, 1, 0],
    [ 0, 0, 0, 1 ]
    ])
    return(z)

#----------------------------------------------------------------------End of math construct.
#initialising the cube:
cube_ini = []

for i in [-1,1]:
    for j in [-1,1]:
        for k in [-1,1]:
            cube_ini.append([i,j,k,1])
cube = np.matrix(np.transpose(cube_ini))

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("3D Camera")
clock = pygame.time.Clock()

#Start of animation code
angle = 0
while True:
    player_pos[0] = m.sin(m.radians(angle)) * 1.5
    angle += 2
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            # print("The program finished running \n \n")
            sys.exit()
    #Creating the projection matrix
    translation_matrix = np.matrix([[ 1 , 0 , 0 , -player_pos[0]],
                          [ 0 , 1 , 0 , -player_pos[1]],
                          [ 0 , 0 , 1 , -player_pos[2]],
                          [ 0, 0, 0, 1 ]])
    rotation_matrix = np.dot(Ry(-camera_rot_y),Rz(-camera_rot_z))
    rotation_matrix = np.dot(Rx(-camera_rot_x),rotation_matrix)
    projection_matrix = np.dot(rotation_matrix,translation_matrix)


    #making the calculation for the projection of the cube
    pos_cam_proj = np.dot(projection_matrix,cube)
    pos_cam_perspective = np.zeros((8,2))
    for i in range(8):
        pos_cam_perspective[i,0] =  (0.5 * HEIGHT * pos_cam_proj[0,i] * (1/m.tan(fov))) /pos_cam_proj[2,i] 
        pos_cam_perspective[i,1] =  (0.5 * HEIGHT * pos_cam_proj[1,i] * (1/m.tan(fov))) /pos_cam_proj[2,i] 

    cube_screen = np.array(pos_cam_perspective)

    #drawing the lines
    screen.fill("Black")
    for i in range(8):
        for j in range(i,8): #
            pygame.draw.line(screen, "white", b(cube_screen[i][0:2]),b(cube_screen[j][0:2]))


    
    pygame.display.update()
    clock.tick(60)

#End of animation code