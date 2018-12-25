import sys

import pygame

from Settings import Settings
from Ship import Ship

def run_game():
    #Initialize game and window
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship
    ship = Ship(screen)

    #Start the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw the screen during each pass through the loop
        screen.fill(game_settings.bg_color)            
        ship.blitme()

        #draw the most recent screen visible
        pygame.display.flip()

run_game()