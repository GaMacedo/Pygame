import pygame

pygame.init()

#Game sizes
GAME_WIDTH = 800
GAME_HEIGH = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

#Map Vars
MAP_WIDHT = 30
MAP_HEIGHT = 30

#Player Position
P_POS_X = 5
P_POS_Y = 5

#Color Definitions
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_GRAY = (100,100,100)

#Game colors
COLOR_DEFAULT_BG = COLOR_GRAY

#Sprites
S_PLAYER = pygame.image.load('Imgs/PLAYER.png')
S_WALL1 = pygame.image.load('Imgs/WALL1.png')
S_FLOOR = pygame.image.load('Imgs/FLOOR1.jpg')