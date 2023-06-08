from ursina import *
from GameParameters import *
from train_spawner import *

class Menu(Entity):
    def __init__(self, player, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)
        self.background = Sprite('assets/menu_background.png', z = -8.9,y =-1, rotation = (180,0,0))
        player.rotation = (180,0,0)
        self.buttons = {
            'start':Button(text= 'Start', scale = (.4,.1), position = (-.65, .15),color = color.black),
            'sterowanie':Button( text='Sterowanie', scale = (.4,.1), position = (-.65,0),color=color.black),
            'wyjdź':Button(text='Wyjdź', scale = (.4,.1), position = (-.65,-.15), color=color.black),
            'title': Text(text='Train Surfers', position=(.15, .30), font="assets/MoiraiOne-Regular.ttf", size=30,
                          scale=3.2)
            }
        self.buttons['start'].on_click=lambda:Func(self.close_menu(player))
        self.buttons['sterowanie'].on_click=lambda :Func(self.controls(player))
        self.buttons['wyjdź'].on_click=lambda:application.quit()
        self.buttons['start'].text_entity.font  = "assets/GasoekOne-Regular.ttf"
        self.buttons['sterowanie'].text_entity.font = "assets/GasoekOne-Regular.ttf"
        self.buttons['wyjdź'].text_entity.font = "assets/GasoekOne-Regular.ttf"
        self.score_point = Text('Score:' + str(GameParameters.score), width=10, height=2, position=(-.09, .4),font  = "assets/BebasNeue-Regular.ttf", scale = 2)
        self.score_point.disable()
        mouse.visible = True

    def close_menu(self, player):
        player.rotation=(0,0,0)
        GameParameters.speed = 20
        GameParameters.paused = False
        GameParameters.score = 0
        GameParameters.can_spawn = True
        self.score_point.enable()
        for i in GameParameters.train:
            i.disable()
        GameParameters.train.clear()
        GameParameters.train += train_generator_init(player)
        for key in self.buttons.keys():
            self.buttons[key].disable()
        mouse.visible = False
    def controls(self,player):
        for key in self.buttons.keys():
            self.buttons[key].disable()
        back = Button(text = 'Wróć do menu',position = (0, -.25), scale = (.4,.1), color = color.black)
        back.text_entity.font  = "assets/GasoekOne-Regular.ttf"
        desc = ("Sterowanie:\n"
                "Ruch w prawo: D lub Prawy Przycisk Myszki\n"
                "Ruch w lewo: A lub Lewy Przycisk Myszki\n"
                "Skok: Spacja, Scroll w górę lub w dół\n"
                "Wyjście do menu: Esc")
        te = Text(desc, width = 8, height = 6, position = (-.3, .4), font = "assets/GasoekOne-Regular.ttf")
        te.create_background()
        objects = (te,back)
        back.on_click= lambda: Func(self.return_menu(player, objects))
        mouse.visible = True
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
        back = Button(text = 'Wróć do menu',position = (0.33, -.25), scale = (.4,.1), color = color.black)
        restart = Button(text= 'Restart', scale = (.4,.1), position = (-.33, -.25),color = color.black)
        back.text_entity.font  = "assets/GasoekOne-Regular.ttf"
        restart.text_entity.font = "assets/GasoekOne-Regular.ttf"
        self.score_point.disable()
        desc = (
            "Game Over!\n"
            'Wynik: ' + str(GameParameters.score)
        )
        te = Text(desc, width=10, height=2,origin=(0,0), position = (0,0.2), font  = "assets/GasoekOne-Regular.ttf")
        objects = (te, back, restart)
        back.on_click = lambda: Func(self.return_menu(player,objects))
        restart.on_click = lambda: Func(self.restart(player, GameParameters,objects))
        mouse.visible = True

    def show_menu(self, player):
        player.rotation = (180, 0, 0)
        GameParameters.paused = True
        for key in self.buttons.keys():
            self.buttons[key].enable()
        mouse.visible = True
    def pause_menu(self, player):
        GameParameters.paused = True
        self.score_point.disable()
        for i in GameParameters.train:
            i.disable()
        temp = player.position
        player.rotation = (180,0,0)
        player.position = (0,0,0)
        back = Button(text = 'Wróć do menu', scale = (.4,.1),position = (-0.65, -.25), color = color.black,)
        restart = Button(text= 'Restart', scale = (.4,.1), position = (0, -.25),color = color.black, font  = "assets/GasoekOne-Regular.ttf")
        resume = Button(text= 'Wznów', scale = (.4,.1), position = (.65, -.25),color = color.black)
        back.text_entity.font = "assets/GasoekOne-Regular.ttf"
        restart.text_entity.font = "assets/GasoekOne-Regular.ttf"
        resume.text_entity.font = "assets/GasoekOne-Regular.ttf"
        te = Text("Pauza", width=10, height=2,origin=(0,0), position = (0,.4),font  = "assets/BebasNeue-Regular.ttf", scale = 1.5)
        t2 = Text("Wynik: "+ str(GameParameters.score), width=10, height=2,origin=(0,0), position = (0,.1),font  = "assets/BebasNeue-Regular.ttf", scale = 1.5)
        objects = (te, back, restart, resume,t2)
        back.on_click = lambda: Func(self.return_menu(player,objects))
        restart.on_click = lambda: Func(self.restart(player, GameParameters,objects))
        resume.on_click = lambda : Func(self.resume(player, objects, temp))
        mouse.visible = True

    def resume(self, player, objects, temp):
        player.position = temp
        player.rotation = (0,0,0)
        GameParameters.paused = False
        self.score_point.enable()
        for i in GameParameters.train:
            i.enable()
        for i in objects:
            i.disable()
        mouse.visible = False

    def restart(self, player, GameParameters, objects):
        GameParameters.score = 0
        GameParameters.can_spawn = True
        GameParameters.speed = 20
        for i in GameParameters.train:
            i.disable()
        GameParameters.train.clear()
        player.position = (0, 0, 0)
        player.rotation = (0, 0, 0)
        for i in objects:
            i.disable()
        self.score_point.enable()
        GameParameters.paused = False
        GameParameters.train += train_generator_init(player)
        mouse.visible = False
