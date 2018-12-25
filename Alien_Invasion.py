import sys

import pygame

from Settings import Settings
from Ship import Ship
import game_functions as gf

def run_game():
    #Initialize game and window
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship
    ship = Ship(screen, game_settings)

    #Start the main game loop
    while True:
        #check for key input
        gf.check_events(ship)
        ship.update()
        gf.update_screen(game_settings, ship, screen)

run_game()