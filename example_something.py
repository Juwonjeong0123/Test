"""import tracemalloc
tracemalloc.start()"""

##############################

from test import GameEngine, GameWindow, Draw, Input, Sprite, rects_collide
from utils import Vector2

window_w = 800
window_h = 800

window = GameWindow(window_w, window_h, title="Test")
canvas = window.get_canvas()
root = window.get_root()
draw = Draw(canvas, root)
input = Input(window.root)
fps = 60

left = Vector2(-1, 0)
right = Vector2(1, 0)
up = Vector2(0, -1)
down = Vector2(0, 1)
zero = Vector2(0, 0)

class Player(Sprite):
    def __init__(self, x, y, width, height, color="black", speed=1):
        super().__init__(x, y, width, height, color, speed)
        self.bullets = []
        self.shoot_colldown = 3
        self.shoot_timer = 0

    def move(self):
        if input.is_key_pressed("Left"):
            vec = left
        elif input.is_key_pressed("Right"):
            vec = right
        elif input.is_key_pressed("Up"):
            vec = up
        elif input.is_key_pressed("Down"):
            vec = down
        else:
            vec = zero

        self.update(vec)
        self.draw(canvas)

    def shoot(self):
        if self.shoot_timer > 0:
            self.shoot_timer -= 1

        if input.is_key_pressed("space") and self.shoot_timer <= 0:
            size = 30

            bullet = Bullet(self.x + (self.width-size)/2, self.y-50, size, size, color="red", speed=30)
            bullet.shoot()
            self.bullets.append(bullet)
            self.shoot_timer = self.shoot_colldown

    """def test(self):
        a = 0
        for b in self.bullets:
            a += 1
        print(a)"""

class Bullet(Sprite):
    def shoot(self):
        vec = up
        self.update(vec)
        self.draw(canvas)

    def is_off_screen(self):
        if self.y + self.height < 0:
            return True
        else:
            False

player_w = 100
player_h = 100
player = Player((window_w-player_w)/2, window_h*3/4, player_w, player_h, color="blue", speed=10)

def update():
    if input.is_key_pressed("q"):
        """snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')

        for stat in top_stats[:5]:
                print(stat)"""
  
        engine.stop()

    

    draw.clear()

    player.move()
    player.shoot()
    # player.test()

    player.bullets = [b for b in player.bullets if not b.is_off_screen()]

    for bullet in player.bullets:
        bullet.shoot()

    window.update()

engine = GameEngine(update_func=update, fps=fps)
engine.start()

    