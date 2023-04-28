from Train import *
from random import *
from GameParameters import *
tablica = [0,0,0]
def train_generator():
    for x in range(random(0,4)):
        for y in x:
            index = random(0,3)
            match index:
                case 0:
                    train = Train(position=(-20, 0, 100), scale=(10, 10, 20))
                case 1:
                    train = Train(position=(0, 0, 100), scale=(10, 10, 20))
                case 2:
                    train = Train(position=(20, 0, 100), scale=(10, 10, 20))
