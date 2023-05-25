from GameParameters import *
from ursina import *
from Player import *
from Train import *
from Menu import *
from screeninfo import get_monitors
from train_spawner import *

GameParameters.paused = True
monitor = get_monitors()
app = Ursina(fullscreen=True)
window.size = Vec2(monitor[0].width, monitor[0].height)
window.fps_counter.disable()
player = Player(collider='box', model='cube', position=(0, 0, 0))
main_menu = Menu(player)
ground = Entity(model='/assets/tracks.glb', collider='box', scale=0.67, position=(0, -7, 50))
player.menu = main_menu
GameParameters.train += train_generator_init(player)


def update():
    if GameParameters.death == True and GameParameters.paused == False:
        for i in GameParameters.train:
            i.disable()
        GameParameters.train.clear()
        main_menu.death_menu(player)
    if GameParameters.paused == False:
        GameParameters.score += int(time.dt * 100)
        main_menu.score_point.text = "Score:" + str(GameParameters.score)
    GameParameters.speed += 0.01
    if (GameParameters.can_spawn == True and GameParameters.paused == False):
        GameParameters.train += train_generator(player)
        GameParameters.can_spawn = False


Sky(texture='assets/night.jpg')
app.run()
