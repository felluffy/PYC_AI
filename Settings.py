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
