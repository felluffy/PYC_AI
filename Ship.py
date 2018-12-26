import pygame 
class Ship():
    def __init__(self, screen, game_settings):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.game_settings = game_settings
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship's postion based on movement flag"""
        #update the ship's center value, not the rect 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.game_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.game_settings.ship_speed_factor

        #uodate rect object from self.center
        self.rect.centerx = self.center 
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect) 