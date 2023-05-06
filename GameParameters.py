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
    speed = 1
    paused = True
    can_spawn = True
