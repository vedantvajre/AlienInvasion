class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.0

        # Bullet settings
        self.bullet_speed_factor = 1.0
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = (0, 255, 0)
