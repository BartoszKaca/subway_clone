#importowanie wszystkich potrzebnych bibliotek i plików
import GameParameters
from GameParameters import *
from ursina import *
from Player import *
from Train import *
from Menu import *
from screeninfo import get_monitors
from train_spawner import *
from high_scores import *

GameParameters.paused = True
#ustawianie pełnego ekranu
monitor = get_monitors()
app = Ursina(fullscreen=True)
window.size = Vec2(monitor[0].width, monitor[0].height)
window.fps_counter.disable()
#incjalizacja obiektów
player = Player(collider='box', model='cube', position=(0, 0, 0))
main_menu = Menu(player)
for i in range(8):
    ground = Entity(model='/assets/tunele.glb', collider='box', scale=0.67, position=(0, -7, 110 *i))
#światło bezpośrednio nad graczem
L = PointLight(y = 10, x = 0, z = 0, color = color.white, shadows = True)
player.menu = main_menu
#wygenerowanie początkowych pociągów
GameParameters.train += train_generator_init(player)
#ustawienie głośnosci
Audio.volume_multiplier = 0.5

def update():
    #przy śmierci usuwanie pociągów i wyświetlanie menu śmierci
    if GameParameters.death == True and GameParameters.paused == False:
        for i in GameParameters.train:
            i.disable()
        GameParameters.train.clear()
        main_menu.death_menu(player)
    #zwiększanie wyniku i szybkości
    if GameParameters.paused == False:
        GameParameters.score += int(time.dt * 100)
        main_menu.score_point.text = "Score:" + str(GameParameters.score)
    GameParameters.speed += 0.01
    #pojawianie się pociągów
    if (GameParameters.can_spawn == True and GameParameters.paused == False):
        GameParameters.train += train_generator(player)
        GameParameters.can_spawn = False


Sky(texture='assets/night.jpg')
app.run()
