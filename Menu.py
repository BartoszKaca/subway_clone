from ursina import *
from GameParameters import *

class Menu(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)
        self.main_menu = Entity(parent = self)
        self.help_menu = Entity(parent = self)
        self.background = Sprite('menu_background.png', z = -8.9,y =-1, rotation = (180,0,0))
        player.rotation = (180,0,0)
        buttons = {
            'start': lambda : Func(self.close_menu(player)),
            'jak to sie kurwa dzieje': lambda :Func(self.kontrole(player)),
            'wyjdz': lambda : application.quit()
        }
        self.bl = ButtonList(buttons, position = (-0.85,0.5), button_height=5, width = .5)

    def close_menu(self, player):
        player.rotation=(0,0,0)
        GameParameters.paused = False
        self.bl.disable()
    def kontrole(self,player):
        player.rotation=(0,0,0)
        GameParameters.paused = False
