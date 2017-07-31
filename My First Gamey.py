import pygame
# import tcod
# game files
import Constants as Cons

#      _______.___________..______       __    __    ______ .___________.
#     /       |           ||   _  \     |  |  |  |  /      ||           |
#    |   (----`---|  |----`|  |_)  |    |  |  |  | |  ,----'`---|  |----`
#     \   \       |  |     |      /     |  |  |  | |  |         |  |
# .----)   |      |  |     |  |\  \----.|  `--'  | |  `----.    |  |
# |_______/       |__|     | _| `._____| \______/   \______|    |__|

class struc_Tile :
    def __init__(self, block_path):
        self.block_path = block_path





# .___  ___.      ___      .______
# |   \/   |     /   \     |   _  \
# |  \  /  |    /  ^  \    |  |_)  |
# |  |\/|  |   /  /_\  \   |   ___/
# |  |  |  |  /  _____  \  |  |
# |__|  |__| /__/     \__\ | _|

def map_create():
    # Create an array 30 x 30 with struct tiles
    new_map =   [[ struc_Tile(False) for y in range (0, Cons.MAP_HEIGHT) ] for x in range (0, Cons.MAP_WIDTH) ]

    # Create 1 wall to debug
    new_map[10][10].block_path = True
    new_map[10][15].block_path = True

    return new_map



# _______  .______          ___   ____    __    ____  __  .__   __.   _______
#|       \ |   _  \        /   \  \   \  /  \  /   / |  | |  \ |  |  /  _____|
#|  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  |  | |   \|  | |  |  __
#|  |  |  ||      /      /  /_\  \  \            /   |  | |  . `  | |  | |_ |
#|  '--'  ||  |\  \----./  _____  \  \    /\    /    |  | |  |\   | |  |__| |
#|_______/ | _| `._____/__/     \__\  \__/  \__/     |__| |__| \__|  \______|

def draw_game():

    global SURFACE_MAIN
    # Clear surface
    SURFACE_MAIN.fill(Cons.COLOR_DEFAULT_BG)

    # Draw the Map
    draw_map(GAME_MAP)

    #Draw the character
    SURFACE_MAIN.blit(Cons.S_PLAYER, (Cons.GAME_WIDTH * 0.5, Cons.GAME_HEIGHT * 0.5))

    # Update the display
    pygame.display.flip()

def draw_map(map_to_draw):

    for x in range (0,Cons.MAP_WIDTH):
        for y in range (0,Cons.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                #Draw wall
                SURFACE_MAIN.blit(Cons.S_WALL, (x*Cons.CELL_WIDHT,y*Cons.CELL_HEIGHT))

            else:
                #Draw floor
                SURFACE_MAIN.blit(Cons.S_FLOOR, (x * Cons.CELL_WIDHT, y * Cons.CELL_HEIGHT))



#  _______      ___      .___  ___.  _______
# /  _____|    /   \     |   \/   | |   ____|
#|  |  __     /  ^  \    |  \  /  | |  |__
#|  | |_ |   /  /_\  \   |  |\/|  | |   __|
#|  |__| |  /  _____  \  |  |  |  | |  |____
# \______| /__/     \__\ |__|  |__| |_______|

def game_main_loop():
    '''In this function, we loop the main game'''

    game_quit = False

    while not game_quit:
        # get input
        events_list = pygame.event.get()


        # process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True

        #Draw the game
        draw_game()

    #Quit the game
    pygame.quit()
    exit()

def game_initialize():
    '''In this Function, Initialize the main window and pygame'''

    global SURFACE_MAIN, GAME_MAP
    # Initialize pygame
    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode( (Cons.GAME_WIDTH,Cons.GAME_HEIGHT) )

    GAME_MAP = map_create()



## Execute the game ##
if __name__ == '__main__':
    game_initialize()
    game_main_loop()