from ursina import *
from Player import *
from Train import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.editor_camera import *
from train_spawner import *

app = Ursina()
player = Player(collider = 'box',model = 'cube', position = (0, 0, 0))
#player = FirstPersonController(collider = 'box',model = 'cube', position = (0, 0, 0))
ground = Entity(model = 'plane', texture = 'tracks.png', collider = 'mesh', scale = (60, 1, 100), position = (0,0,50))
train = train_generator(player)
#plus = Entity(model = 'cube', texture = 'brick', scale = (10,10,20), collider = 'box', position = (0,0,0))
Sky()
print()
def update():
    print(distance_z(player, train), distance_y(player,train), distance_x(player, train))
app.run()