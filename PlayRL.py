import pygame

#Game files
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
    SURFACE_MAIN.blit(Constants.S_PLAYER, (Constants.P_POS_X,Constants.P_POS_Y))

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

        #Player movement
        if (pygame.key.get_pressed()[pygame.K_UP] != 0):
            Constants.P_POS_Y = Constants.P_POS_Y - 0.5
        if (pygame.key.get_pressed()[pygame.K_DOWN] != 0):
            Constants.P_POS_Y = Constants.P_POS_Y + 0.5
        if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
            Constants.P_POS_X = Constants.P_POS_X + 0.5
        if (pygame.key.get_pressed()[pygame.K_LEFT] != 0):
            Constants.P_POS_X = Constants.P_POS_X - 0.5

        # Draw the map
        # Draw_map(GAME_MAP)

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

    global SURFACE_MAIN, GAME_MAP

    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((Constants.GAME_WIDTH,Constants.GAME_HEIGH))
    GAME_MAP = map_create()




if __name__ == "__main__":
    game_initialize()
    game_main_loop()

