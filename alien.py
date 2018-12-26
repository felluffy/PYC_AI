#Credit to MillionthVector for the sprite
#link to his works http://millionthvector.blogspot.de 
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in the fleet"""
    
    def __init__(self, game_settings, screen):
        """initialize the alient and its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        #load the alien and image and set its rect attribiute
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height / 10

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
