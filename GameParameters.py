from ursina import *
#algorytm sortujący używany przy tablicy wyników
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array
#kalkulowanie dystansu w osi x między poszczególnymi obiektami
def distance_x(a, b):
    if hasattr(a, 'position'): a = a.position
    if hasattr(b, 'position'): b = b.position
    return sqrt((b[0] - a[0])**2)
#kalkulowanie dystansu w osi z między poszczególnymi obiektami
def distance_z(a,b):
    if hasattr(a, 'position'): a = a.position
    if hasattr(b, 'position'): b = b.position
    return sqrt((b[2] - a[2])**2)
#kalkulowanie dystansu w osi y między poszczególnymi obiektami
def distance_y(a,b):
    if hasattr(a, 'position'): a = a.position
    if hasattr(b, 'position'): b = b.position
    return sqrt((b[1]-a[1])**2)
#klasa przechowująca informacje o grze
class GameParameters():
    speed = 20
    paused = True
    can_spawn = True
    score = 0
    death = False
    train = []


