from ursina import *

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array
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
    train = []


