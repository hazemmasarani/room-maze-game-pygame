import pygame

# Initialize Pygame
pygame.init()

##########################
###### Constants #########
##########################

# Get the current screen dimensions
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
BACKGROUND_COLOR = (0, 0, 255)  # Black

# Create a screen with the current dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Room Maze Pygame")

##########################
####### Game loop ########
##########################
running = True
while running:

    ##########################
    ##### Event Handling #####
    ##########################

    # Event handling to check if user want to end the game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    
    ##########################
    ## Updating Game State ###
    ##########################



    ##########################
    ####### Rendering ########
    ##########################

    

##########################
####### Clean up #########
##########################
pygame.quit()
