from ursina import *
def distance_x(a, b):
    if hasattr(a, 'position'): a = a.position
    if hasattr(b, 'position'): b = b.position
    return sqrt((b[0] - a[0])**2)
def distance_z(a,b):
    if hasattr(a, 'position'): a = a.position
    if hasattr(b, 'position'): b = b.position
    return sqrt((b[2] - a[2])**2)
def distance_y(a,b):
    if hasattr(a, 'position'): a = a.position
    if hasattr(b, 'position'): b = b.position
    return sqrt((b[1]-a[1])**2)

class GameParameters():
    speed = 20
    paused = True
    can_spawn = True
    score = 0
    death = False

    def restart(self, player, menu, objects):
        self.score = 0
        self.paused = True
        self.death = True
        self.can_spawn = True
        self.speed = 20
        player.position = (0,0,0)
        player.rotation = (0,0,0)
        for i in objects:
            i.disable()
        menu.score_point.enable()
