from Train import *
from random import *
from GameParameters import *
tablica = [0,0,0]
def train_generator(player):
    for x in range(random.randrange(1,4)):
            index = random.randrange(0,3)
            match index:
                case 0:
                    train = Train(position=(-20, 0, 100), scale=(10, 10, 20), player_info=player)
                case 1:
                    train = Train(position=(0, 0, 100), scale=(10, 10, 20),player_info=player)
                case 2:
                    train = Train(position=(20, 0, 100), scale=(10, 10, 20),player_info=player)
    return train