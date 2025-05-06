from test import GameEngine, GameWindow, Draw, Input

window = GameWindow(width=640, height=480, title="My Game")
canvas = window.get_canvas()
root = window.get_root()
draw = Draw(canvas, root)
input_handler = Input(window.root)

def update(): #직접 업뎃 함수 정의
    draw.clear()

    if input_handler.is_key_pressed("Left"):
        color = "blue"
    else:
        color = "red"

    draw.image(img_path="./jotaro.jpg")

    draw.rect(100, 100, 100, 100, fill=color)
    window.update()

engine = GameEngine(update_func=update, fps=60) #넣다
engine.start() #시발점
