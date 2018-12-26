import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game_settings, screen, ship):
        """create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        #create a bullet recct at (0, 0) and then set current position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)