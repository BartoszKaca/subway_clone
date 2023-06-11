from ursina import *

from GameParameters import *
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        #parametry klasy gracza
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
        self.menu = None
        for key, value in kwargs.items():
            setattr(self, key, value)
    #kontrola grawitacji i pozycji
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
            #skok
            if key == 'space' or key == 'scroll up' or key =='scroll down':
                if(self.y<1 or self.y ==7 and self.air_time ==0 ):
                     self.jump()
            #ruch w lewo
            if key == 'a' or key =='left mouse down':
                if (self.x==0 or self.x==20 or self.x==-20):
                    self.move_left()
            #ruch w prawo
            if key == 'd' or key =='right mouse down':
                if (self.x == 0 or self.x == 20 or self.x == -20):
                    self.move_right()
            #menu pauzy
            if key == 'escape':
                self.menu.pause_menu(self)

    #obsługa skoku
    def jump(self):
        self.animate_y(self.y + 15,duration=.4)
    #obsługa ruchu w prawo
    def move_right(self):
        if(self.x<=0):
            self.animate_x(self.x +20,duration = .1)
    #obsługa ruchu w lewo
    def move_left(self):
        if(self.x>=0):
            self.animate_x(self.x-20, duration = .1)

