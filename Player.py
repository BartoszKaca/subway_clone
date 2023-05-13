from ursina import *
from GameParameters import *
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.paused = False
        self.height = 1
        self.gravity = 1
        self.camera_pivot = Entity(parent=self, y = self.height)
        camera.parent = self.camera_pivot
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        self.air_time = 0
        self.grav_test = 0
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(1,1,1))
        for key, value in kwargs.items():
            setattr(self, key, value)
    def update(self):
        if(self.y >= 10):
            self.grav_test = 1
        if(self.grav_test == 1):
            self.y -= min(self.air_time, self.y - .05) * time.dt * 100
            self.air_time += time.dt * .5 * self.gravity
        if (self.y < 0.5):
            self.air_time = 0
            self.y = 0
            self.grav_test = 0
        self.paused = GameParameters.paused
        if self.paused == True:
            self.y = 0

    def input(self, key):
        if(self.paused == False):
            if key == 'space' or key == 'scroll up' or key =='scroll down':
                if(self.y<1 or self.y ==5 and self.air_time ==0 ):
                     self.jump()
            if key == 'a' or key =='left mouse down':
                if (self.x==0 or self.x==20 or self.x==-20):
                    self.move_left()
            if key == 'd' or key =='right mouse down':
                if (self.x == 0 or self.x == 20 or self.x == -20):
                    self.move_right()

    def jump(self):
        self.animate_y(self.y + 15,duration=.25)
    def move_right(self):
        if(self.x<=0):
            self.animate_x(self.x +20,duration = .1)
    def move_left(self):
        if(self.x>=0):
            self.animate_x(self.x-20, duration = .1)

