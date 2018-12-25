import sys

import pygame

def run_game():
    #Initialize game and window
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Alien Invasion")

    #background color
    bg_color = (230, 230, 230)

    #Start the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw the screen during each pass through the loop
        screen.fill(bg_color)            

        #draw the most recent screen visible
        pygame.display.flip()

run_game()