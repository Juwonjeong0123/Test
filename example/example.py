"""import tracemalloc
tracemalloc.start()"""

##############################

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from test import GameEngine, GameWindow, Draw, Input, Sprite, rects_collide
from utils import Vector2

window_w = 600
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
    def __init__(self, x, y, width, height, color="black", speed=1, hp = 1000):
        super().__init__(x, y, width, height, color, speed)
        self.hp = hp
        self.bullets = []
        self.shoot_colldown = 3
        self.shoot_timer = 0
        self.vec = zero

    def qwer(self):
        self.vec.x = 0
        self.vec.y = 0

        # 가로 방향
        if input.is_key_pressed("a"):
            if self.x > 0:
                self.vec.x = -1
        elif input.is_key_pressed("d"):
            if self.x + self.width < window_w:
                self.vec.x = 1

        # 세로 방향
        if input.is_key_pressed("w"):
            if self.y > 0:
                self.vec.y = -1
        elif input.is_key_pressed("s"):
            if self.y + self.height < window_h:
                self.vec.y = 1

    def move(self):
        self.update(self.vec)
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

class Enemy(Sprite):
    def __init__(self, x, y, width, height, color="black", speed=1, hp=10000):
        super().__init__(x, y, width, height, color, speed)
        self.hp = hp

    def zxcv(self):
        # self.update()
        self.draw(canvas)

    def You_Suck(self, bullet):
        if rects_collide(self.get_rect(), bullet.get_rect()):
                self.hp -= 10

    def test(self):
        self.width = 500
        self.height = 500

player_w = 100
player_h = 100
enemy_w = 100
enemy_h = 100
player = Player((window_w-player_w)/2, window_h*3/4, player_w, player_h, color="blue", speed=15, hp=1000)
enemy = Enemy((window_w-enemy_w)/2, window_h*1/4, enemy_w, enemy_h, color="red", speed="10", hp=1000)

def update():
    if input.is_key_pressed("q"):
        """snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')

        for stat in top_stats[:5]:
                print(stat)"""
  
        engine.stop()

    

    draw.clear()

    player.qwer()
    player.move()
    player.shoot()
    # player.test()
    if enemy.hp <= 0:
        enemy.test()
    enemy.zxcv()

    player.bullets = [b for b in player.bullets if not b.is_off_screen()]

    for bullet in player.bullets:
        bullet.shoot()
        enemy.You_Suck(bullet)

    window.update()

engine = GameEngine(root, update_func=update, fps=fps)
engine.start()

    