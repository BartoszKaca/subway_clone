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
        self.buttons['sterowanie'].on_click=lambda :Func(self.controls(player))
        self.buttons['wyjdź'].on_click=lambda:application.quit()
        self.score_point = Text('Score:' + str(GameParameters.score), width=10, height=2, position=(.5, .4))
        self.score_point.disable()

    def close_menu(self, player):
        player.rotation=(0,0,0)
        GameParameters.speed = 20
        GameParameters.paused = False
        GameParameters.score = 0
        GameParameters.can_spawn = True
        self.score_point.enable()
        for key in self.buttons.keys():
            self.buttons[key].disable()
    def controls(self,player):
        for key in self.buttons.keys():
            self.buttons[key].disable()
        back = Button(text = 'wroc do menu',position = (-0.65, .4), scale = (.4,.1), color = color.black)
        desc = ("Sterowanie:\n"
                "ruch w prawo: D lub Prawy Przycisk Myszki\n"
                "ruch w lewo: A lub Lewy Przycisk Myszki\n"
                "Skok: Spacja, Scroll w górę lub w dół\n"
                "Wyjście do menu: Esc")
        te = Text(desc, width = 8, height = 6, position = (-.3, .4))
        te.create_background()
        objects = (te,back)
        back.on_click= lambda: Func(self.return_menu(player, objects))
    def return_menu(self, player, objects):
        for i in objects:
            i.disable()
        self.show_menu(player)
    def death_menu(self, player):
        GameParameters.death = False
        GameParameters.paused = True
        player.air_time = 0
        player.position = (0,0,0)
        player.rotation = (180,0,0)
        back = Button(text = 'wroc do menu',position = (-0.65, .4), scale = (.4,.1), color = color.black)
        restart = Button(text= 'restart', scale = (.4,.1), position = (-.65, .15),color = color.black)
        self.score_point.disable()
        desc = (
            "Game Over!\n"
            'Score: ' + str(GameParameters.score)
        )
        te = Text(desc, width=10, height=2,origin=(0,0), position = (0,0.2))
        objects = (te, back, restart)
        back.on_click = lambda: Func(self.return_menu(player,objects))
        restart.on_click = lambda: Func(GameParameters.restart(GameParameters, player, self,objects))
        te.create_background()

    def show_menu(self, player):
        player.rotation = (180, 0, 0)
        GameParameters.paused = True
        for key in self.buttons.keys():
            self.buttons[key].enable()