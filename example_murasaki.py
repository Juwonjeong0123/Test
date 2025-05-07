from test import GameEngine, GameWindow, Draw, Input, Sprite, rects_collide
from utils import Vector2

window = GameWindow(width=1920, height=1080, title="Game")
canvas = window.get_canvas()
root = window.get_root()
draw = Draw(canvas, root)
input_handler = Input(window.root)

player = Sprite(50, 50, 100, 100, color="blue", speed=10)
gay = Sprite(300, 50, 100, 100, color="red", speed=10)

def update(): #직접 업뎃 함수 정의
    draw.clear()

    if input_handler.is_key_pressed("Left"):
        vec = Vector2(-1, 0)
    elif input_handler.is_key_pressed("Right"):
        vec = Vector2(1, 0)
    elif input_handler.is_key_pressed("Up"):
        vec = Vector2(0, -1)
    elif input_handler.is_key_pressed("Down"):
        vec = Vector2(0, 1)
    else:
        vec = Vector2(0, 0)

    if input_handler.is_key_pressed("a"):
        vec2 = Vector2(-1, 0)
    elif input_handler.is_key_pressed("d"):
        vec2 = Vector2(1, 0)
    elif input_handler.is_key_pressed("w"):
        vec2 = Vector2(0, -1)
    elif input_handler.is_key_pressed("s"):
        vec2 = Vector2(0, 1)
    else:
        vec2 = Vector2(0, 0)

    if rects_collide(player.get_rect(), gay.get_rect()):
        player.color = "purple"
        gay.color = "purple"
    else:
        player.color = "blue"
        gay.color = "red"

    player.update(vec)
    player.draw(canvas)

    gay.update(vec2)
    gay.draw(canvas)

    window.update()

engine = GameEngine(update_func=update, fps=60) #넣다
engine.start() #시발점
