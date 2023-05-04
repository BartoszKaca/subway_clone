from ursina import *

class Menu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)
        self.main_menu = Entity(parent = self)
        self.help_menu = Entity(parent = self)
        self.background = Sprite('menu_background.png', z = 10)
