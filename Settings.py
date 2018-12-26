class Settings():
    """Class to store all settings for the game"""
    def __init__(self):
        """initialize game's settings"""
        #screen settings
        self.width = 1280
        self.height = 720
        self.bg_color = (0, 0, 0) #background color

        #ship settings 
        self.ship_speed_factor = 1.4

        #bullet settings 
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #limit number of bullets
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right, -1 left
        self.fleet_direction = 1

