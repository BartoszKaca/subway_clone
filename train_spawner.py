from Train import *
from random import *
from GameParameters import *

def train_generator(player):
    if(GameParameters.paused == False):
        for x in range(random.randrange(1,4)):
            index = random.randrange(0,3)
            match index:
                case 0:
                    train = Train(position=(-20, 0, 500), scale=(10, 10, 40), player_info=player)
                case 1:
                    train = Train(position=(0, 0, 500), scale=(10, 10, 40),player_info=player)
                case 2:
                    train = Train(position=(20, 0, 500), scale=(10, 10, 40),player_info=player)
        GameParameters.can_spawn = False
        return train