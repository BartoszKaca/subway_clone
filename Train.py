from ursina import *
from GameParameters import *

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