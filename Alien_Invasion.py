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

    #make a group to store bullets in
    bullets = pygame.sprite.Group()

    #make a group of  aliens
    aliens = pygame.sprite.Group()
    gf.create_fleet(game_settings, screen, aliens, ship)

    #Start the main game loop
    while True:
        #check for key input
        gf.check_events(game_settings, ship, screen, bullets)
        ship.update()
        gf.update_bullets(game_settings, screen, bullets, aliens)
        gf.update_aliens(game_settings, ship, aliens)
        gf.update_screen(game_settings, ship, aliens, screen, bullets)

run_game()