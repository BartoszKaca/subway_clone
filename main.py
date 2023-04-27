from ursina import *
from Player import *
from Train import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.editor_camera import *

app = Ursina()
player = Player(collider = 'box',model = 'cube', position = (0, 0, 0))
#player = FirstPersonController(collider = 'box',model = 'cube', position = (0, 0, 0))
ground = Entity(model = 'plane', texture = 'tracks.png', collider = 'mesh', scale = (60, 1, 100), position = (0,0,50))
train = Train(position = (0, 0, 100), scale = (10,10,20))
#plus = Entity(model = 'cube', texture = 'brick', scale = (10,10,20), collider = 'box', position = (0,0,0))
Sky()

def update():
    if(player.x == train.x and distance_z(player, train)<=10 and distance_y(player,train)<5):
        print("game over")
    elif(player.x == train.x and distance_z(player, train)<=10 and distance_y(player,train)>=5):
        if(player.y<=6):
            player.grav_test=0
            player.y = 5
            player.air_time=0
    elif (player.x == train.x and distance_z(player, train) > 10 and distance_y(player, train)>= 5):
        player.grav_test = 1
    if(player.x != train.x and player.y==5and player.grav_test==0):
        player.grav_test=1
    print(distance_z(player, train), distance_y(player,train))
app.run()