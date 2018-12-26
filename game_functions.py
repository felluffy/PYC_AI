import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, ship, screen, bullets):
    """"respond to keypresses"""
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
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)

def check_keyup_events(event, game_settings, ship, screen, bullets):
    """respond to key releases"""
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
    


def check_events(game_settings, ship, screen, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, ship, screen, bullets)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, game_settings, ship, screen, bullets)
            

def update_screen(game_settings, ship, aliens, screen, bullets):
    #redraw the screen during each pass through the loop
    screen.fill(game_settings.bg_color)            
    
    #redraw all bullets behind ship and aliens 
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #draw the most recent screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """update postion of bullets and get rid of old ones """
    bullets.update()
    #get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        #create a new bullet and add it to the bullets group
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (game_settings.height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (alien_height)) 
    print(number_rows)
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    #alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = (alien.rect.height / 5) +  1.3 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, aliens, ship):
    """create a fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #space between each alien is half an alien
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    #create the row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)