import GameParameters
from ursina import *
from Player import *
from Train import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.editor_camera import *
from train_spawner import *
from Menu import *

app = Ursina()
player = Player(collider = 'box',model = 'cube', position = (0, 0, 0))
main_menu = Menu(player)
ground = Entity(model = 'plane', texture = 'assets/tracks.png', collider = 'mesh', scale = (60, 1, 100), position = (0,0,50))

def update():
    if GameParameters.death == True:
        main_menu.death_menu(player)
    if GameParameters.paused == False:
        GameParameters.score += int(time.dt * 100)
        main_menu.score_point.text = "Score:" + str(GameParameters.score)
    GameParameters.speed += 0.01
    if(GameParameters.can_spawn == True):
        train = train_generator(player)
Sky()
app.run()