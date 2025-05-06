from test import GameEngine, GameWindow, Draw, Input, Sprite, rects_collide
from utils import Vector2

window = GameWindow(width=640, height=480, title="My Game")
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
    else:
        vec = Vector2(0, 0)

    if rects_collide(player.get_rect(), gay.get_rect()):
        player.color = "purple"
        gay.color = "purple"
    else:
        player.color = "blue"
        gay.color = "red"

    player.move(vec)
    player.draw(canvas)

    gay.move(Vector2(0, 0))
    gay.draw(canvas)

    window.update()

engine = GameEngine(update_func=update, fps=60) #넣다
engine.start() #시발점
