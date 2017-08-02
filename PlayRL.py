import pygame
import libtcodpy as libtcod
# Game files
import Constants


#   ______
#  / _____) _                       _
# ( (____ _| |_  ____ _   _  ____ _| |_
#  \____ (_   _)/ ___) | | |/ ___|_   _)
#  _____) )| |_| |   | |_| ( (___  | |_
# (______/  \__)_|   |____/ \____)  \__)


class struct_Tile:
    def __init__(self, block_path):
        self.block_path = block_path


#    ___ _     _           _
#   /___\ |__ (_) ___  ___| |_ ___
#  //  // '_ \| |/ _ \/ __| __/ __|
# / \_//| |_) | |  __/ (__| |_\__ \
# \___/ |_.__// |\___|\___|\__|___/
#           |__/

class obj_Actor:
    def __init__(self, x, y, sprite):
        self.x = x   # Map address
        self.y = y
        self.sprite = sprite

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x * Constants.CELL_WIDTH, self.y * Constants.CELL_HEIGHT))

    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy




#  _______
# (_______)
#  _  _  _ _____ ____
# | ||_|| (____ |  _ \
# | |   | / ___ | |_| |
# |_|   |_\_____|  __/
#               |_|

def map_create():
    new_map = [[struct_Tile(False) for y in range(0, Constants.MAP_HEIGHT)] for x in range(0, Constants.MAP_WIDHT)]

    new_map[10][10].block_path = True
    new_map[10][12].block_path = True

    return new_map

#  ______                   _
# (______)                 (_)
#  _     _ ____ _____ _ _ _ _ ____   ____
# | |   | / ___|____ | | | | |  _ \ / _  |
# | |__/ / |   / ___ | | | | | | | ( (_| |
# |_____/|_|   \_____|\___/|_|_| |_|\___ |
#                                  (_____|


def draw_game():

    global SURFACE_MAIN

    #Clear the surface
    SURFACE_MAIN.fill(Constants.COLOR_DEFAULT_BG)

    #Draw the map
    draw_map(GAME_MAP)

    #Draw the character
    PLAYER.draw()

    #Update display
    pygame.display.flip()

def draw_map(map_to_draw):
    for x in range(0, Constants.MAP_WIDHT):
        for y in range(0, Constants.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                #draw wall
                SURFACE_MAIN.blit(Constants.S_WALL1, (x*Constants.CELL_WIDTH,y*Constants.CELL_HEIGHT))
            else:
                #draw floor
                SURFACE_MAIN.blit(Constants.S_FLOOR, (x*Constants.CELL_WIDTH,y*Constants.CELL_HEIGHT))


#  _______
# (_______)
#  _   ___ _____ ____  _____
# | | (_  (____ |    \| ___ |
# | |___) / ___ | | | | ____|
#  \_____/\_____|_|_|_|_____)

def game_main_loop():
    '''In this function, we loop the main game'''

    game_quit = False

    while not game_quit:
        # get player input
        event_list = pygame.event.get()

        #Process input
        for event in event_list:
            if event.type == pygame.QUIT:
                game_quit = True

            # Move Player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k or event.key == pygame.K_KP8:
                    PLAYER.move(0, -1)
                if event.key == pygame.K_j or event.key == pygame.K_KP2:
                    PLAYER.move(0, 1)
                if event.key == pygame.K_l or event.key == pygame.K_KP6:
                    PLAYER.move(1, 0)
                if event.key == pygame.K_h or event.key == pygame.K_KP4:
                    PLAYER.move(-1, 0)
                if event.key == pygame.K_u or event.key == pygame.K_KP9:
                    PLAYER.move(1, -1)
                if event.key == pygame.K_y or event.key == pygame.K_KP7:
                    PLAYER.move(-1, -1)
                if event.key == pygame.K_n or event.key == pygame.K_KP3:
                    PLAYER.move(1, 1)
                if event.key == pygame.K_b or event.key == pygame.K_KP1:
                    PLAYER.move(-1, 1)


        #Draw the game
        draw_game()

    # quit the game
    pygame.quit()
    exit()

#  _       _
# | |     (_)  _
# | |____  _ _| |_
# | |  _ \| (_   _)
# | | | | | | | |_
# |_|_| |_|_|  \__)

def game_initialize():
    '''This function initialize the game'''

    global SURFACE_MAIN, GAME_MAP, PLAYER

    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((Constants.GAME_WIDTH,Constants.GAME_HEIGH))
    GAME_MAP = map_create()

    PLAYER = obj_Actor(Constants.P_POS_X,Constants.P_POS_Y,Constants.S_PLAYER)




if __name__ == "__main__":
    game_initialize()
    game_main_loop()

