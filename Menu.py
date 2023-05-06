from ursina import *
from GameParameters import *

class Menu(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)
        self.background = Sprite('assets/menu_background.png', z = -8.9,y =-1, rotation = (180,0,0))
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
        back = Button(text = 'wroc do menu',position = (-0.65, .4), scale = (.4,.1), color = color.black)
        desc = ("Sterowanie:\n"
                "ruch w prawo: D lub Prawy Przycisk Myszki\n"
                "ruch w lewo: A lub Lewy Przycisk Myszki\n"
                "Skok: Spacja, Scroll w górę lub w dół\n")
        te = Text(desc, width = 8, height = 6, position = (-.3, .4))
        te.create_background()
        back.on_click= lambda: Func(self.return_menu(player, back,te))
    def return_menu(self, player, back, te):
        back.disable()
        te.disable()
        self.show_menu(player)


    def show_menu(self, player):
        player.rotation = (180, 0, 0)
        GameParameters.paused = True
        for key in self.buttons.keys():
            self.buttons[key].enable()