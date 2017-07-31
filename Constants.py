import pygame

pygame.init()

#Game Sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600
CELL_WIDHT = 32
CELL_HEIGHT = 32

#MAP VARS
MAP_WIDTH = 30
MAP_HEIGHT = 30

#Color Definitions
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_GREY = (100,100,100)

#Game Colors
COLOR_DEFAULT_BG = COLOR_GREY

#Sprites
S_PLAYER = pygame.image.load('Imgs/PLAYER.png')
S_WALL = pygame.image.load('Imgs/WALL1.png')
S_FLOOR = pygame.image.load('Imgs/FLOOR1.png')
