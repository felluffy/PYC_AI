import pygame 
class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.movement_speed = .5

    def update(self):
        """Update ship's postion based on movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.bottom -= 1
        if self.moving_down:
            self.rect.bottom += 1

    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect) 