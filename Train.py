import GameParameters

from ursina import *
from GameParameters import *
from Player import *

class Train(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.paused = False
        self.changed = False
        self.model = 'cube'
        self.texture = 'brick'
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(10,10,20))
        for key, value in kwargs.items():
            setattr(self, key, value)
    def update(self):
        if(self.z >-20 and self.paused == False):
            self.z -= time.dt * GameParameters.speed
        self.hit_info(self.player_info)
        self.paused = GameParameters.paused
        if self.z < 70 and self.changed == False:
            self.changed = True
            GameParameters.can_spawn = True

    def hit_info(self, player):
        if (player.x == self.x and distance_z(player, self) <= 10 and distance_y(player, self) < 5):
            print("game over")
            GameParameters.paused = True
            GameParameters.death = True
        elif (player.x == self.x and distance_z(player, self) <= 10 and distance_y(player, self) >= 5):
            if (player.y <= 6):
                player.grav_test = 0
                player.y = 5
                player.air_time = 0
        elif (player.x == self.x and distance_z(player, self) > 10 and distance_y(player, self) >= 5):
            player.grav_test = 1
        if (player.x != self.x and player.y == 5 and player.grav_test == 0):
            player.grav_test = 1