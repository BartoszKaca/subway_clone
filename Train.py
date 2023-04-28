from ursina import *
from GameParameters import *
from Player import *

class Train(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.texture = 'brick'
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(10,10,20))
        for key, value in kwargs.items():
            setattr(self, key, value)
    def update(self):
        if(self.z >-20):
            self.z -= time.dt * 10 * GameParameters.speed
        self.hit_info(self, self.player_info)

    def hit_info(train, player):
        if (player.x == train.x and distance_z(player, train) <= 10 and distance_y(player, train) < 5):
            print("game over")
        elif (player.x == train.x and distance_z(player, train) <= 10 and distance_y(player, train) >= 5):
            if (player.y <= 6):
                player.grav_test = 0
                player.y = 5
                player.air_time = 0
        elif (player.x == train.x and distance_z(player, train) > 10 and distance_y(player, train) >= 5):
            player.grav_test = 1
        if (player.x != train.x and player.y == 5 and player.grav_test == 0):
            player.grav_test = 1