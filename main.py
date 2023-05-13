import GameParameters
from ursina import *
from Player import *
from Train import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.editor_camera import *
from train_spawner import *
from Menu import *
from screeninfo import get_monitors


monitor = get_monitors()
app = Ursina( fullscreen = True)
window.size = Vec2(monitor[0].width, monitor[0].height)
window.fps_counter.disable()
player = Player(collider = 'box',model = 'cube', position = (0, 0, 0))
main_menu = Menu(player)
ground = Entity(model = '/assets/tracks.glb', collider = 'box', scale = 0.67, position = (0,-7,50))
scene.fog_density = .001
scene.fog_color = color.black


def update():
    print(player.position)
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