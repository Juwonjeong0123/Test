"""import tracemalloc
tracemalloc.start()"""

##############################

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from test import GameEngine, GameWindow, Draw, Input, Sprite, rects_collide
from utils import Vector2

import random

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

            bullet = Bullet(self.x + (self.width-size)/2, self.y-50, size, size, color="purple", speed=30)
            self.bullets.append(bullet)
            bullet2 = Bullet((self.x + (self.width-size)/2) - 60, self.y-50, size, size, color="purple", speed=30)
            self.bullets.append(bullet2)
            bullet3 = Bullet((self.x + (self.width-size)/2) + 60, self.y-50, size, size, color="purple", speed=30)
            self.bullets.append(bullet3)
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

class Enemyfactory():
    def __init__(self):
        self.enemies = []
        self.colldown = 20
        self.timer = 0

    def create_enemy(self):
        if self.timer > 0:
            self.timer -= 1

        if self.timer <= 0:
            w = 50
            h = 50
            x = random.randint(0, window_w - w)
            y = 10

            enemy = Enemy(x, y, w, h, color="red", speed=10, hp=100)
            self.enemies.append(enemy)
            self.timer = self.colldown

    def test(self):
        a = 0
        for e in self.enemies:
            a += 1
        print(a)

class Enemy(Sprite):
    def __init__(self, x, y, width, height, color="black", speed=10, hp=50):
        super().__init__(x, y, width, height, color, speed)
        self.hp = hp

    def asdf(self, bullet):
        if rects_collide(self.get_rect(), bullet.get_rect()):
                self.hp -= 10

    def zxcv(self):
        vec = down
        self.update(vec)
        self.draw(canvas)

    def qwer(self):
        return self.hp <= 0
    
    def is_off_screen(self):
        if self.y > window_h:
            return True
        else:
            False

player_w = 100
player_h = 100
enemy_w = 100
enemy_h = 100
player = Player((window_w-player_w)/2, window_h*3/4, player_w, player_h, color="blue", speed=15, hp=1000)
enemyfactory = Enemyfactory()

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

    # enemyfactory.test()
    
    enemyfactory.create_enemy()

    player.bullets = [b for b in player.bullets if not b.is_off_screen()]
    enemyfactory.enemies = [e for e in enemyfactory.enemies if not e.qwer()]
    enemyfactory.enemies = [e for e in enemyfactory.enemies if not e.is_off_screen()]

    for bullet in player.bullets:
        bullet.shoot()
        for enemy in enemyfactory.enemies:
                enemy.asdf(bullet)

    for enemy in enemyfactory.enemies:
                enemy.zxcv()
    

    window.update()

engine = GameEngine(root, update_func=update, fps=fps)
engine.start()

    