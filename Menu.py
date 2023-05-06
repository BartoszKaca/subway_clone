from ursina import *
from GameParameters import *

class Menu(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)
        self.main_menu = Entity(parent = self)
        self.help_menu = Entity(parent = self)
        self.background = Sprite('menu_background.png', z = -8.9,y =-1, rotation = (180,0,0))
        player.rotation = (180,0,0)
        self.buttons = {
            'start':Button(text= 'start', scale = (.4,.1), position = (-.65, .15),color = color.black),
            'sterowanie':Button( text='sterowanie', scale = (.4,.1), position = (-.65,0),color=color.black),
            'wyjdź':Button(text='wyjdź', scale = (.4,.1), position = (-.65,-.15), color=color.black)
        }
        self.buttons['start'].on_click=lambda:Func(self.close_menu(player))
        self.buttons['sterowanie'].on_click=lambda :Func(self.kontrole(player))
        self.buttons['wyjdź'].on_click=lambda:application.quit()

    def close_menu(self, player):
        player.rotation=(0,0,0)
        GameParameters.paused = False
        for key in self.buttons.keys():
            self.buttons[key].disable()
    def kontrole(self,player):
        for key in self.buttons.keys():
            self.buttons[key].disable()
    def show_menu(self, player):
        player.rotation=(180,0,0)
        GameParameters.paused = True
        for key in self.buttons.keys():
            self.buttons[key].enable()