from Train import *
from random import *
from GameParameters import *
tablica = [0,0,0]
def train_generator():
    for x in range(random(0,4)):
        for y in x:
            index = random(0,3)

