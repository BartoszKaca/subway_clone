from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player_Model(Entity):
    def __init__(self,**kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent = self.controller)
        self.model = 'cube'
        self.texture = 'brick'
        self.weapon_gun = Entity(parent = self.controller.camera_pivot,
                                 scale = 0.13,
                                 position = Vec3(0.7, -0.7, 1.5),
                                 rotation = Vec3(0, 0, 0),
                                 model = 'cube',
                                 texture = 'brick',
                                 visible = False,
                                 full_auto = False)