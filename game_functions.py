import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                #move ship to right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #move ship to left
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                #move ship up
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                #move ship down
                ship.moving_down = True
    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                #move ship to left
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                #move ship up
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                #move ship down
                ship.moving_down = False

def update_screen(game_settings, ship, screen):
    #redraw the screen during each pass through the loop
    screen.fill(game_settings.bg_color)            
    ship.blitme()

    #draw the most recent screen visible
    pygame.display.flip()
