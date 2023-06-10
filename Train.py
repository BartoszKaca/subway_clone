import GameParameters

from ursina import *
from GameParameters import *
from Player import *

class Train(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.paused = False
        self.changed = False
        self.model = '/assets/wagon.glb'
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(10,10,50))
        for key, value in kwargs.items():
            setattr(self, key, value)
    def update(self):
        if self.z <= -100:
            self.disable()
        if self.paused == False:
            self.z -= time.dt * GameParameters.speed
        self.hit_info(self.player_info)
        self.paused = GameParameters.paused
        if self.z < 350 and self.changed == False:
            self.changed = True
            GameParameters.can_spawn = True

    def hit_info(self, player):
        if (player.x == self.x and distance_z(player, self) <= 65 and distance_y(player, self) < 5 and GameParameters.paused == False):
            self.disable()
            GameParameters.paused = False
            GameParameters.death = True
        elif (player.x == self.x and distance_z(player, self) <= 65 and distance_y(player, self) >= 5):
            if (player.y <= 8):
                player.grav_test = 0
                player.y = 7
                player.air_time = 0
        elif (player.x == self.x and distance_z(player, self) > 65 and distance_y(player, self) >= 5):
            player.grav_test = 1
        if (player.x != self.x and player.y == 7 and player.grav_test == 0):
            player.grav_test = 1