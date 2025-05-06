from test import GameEngine, GameWindow, Draw, Input

window = GameWindow(width=640, height=480, title="My Game")
canvas = window.get_canvas()
root = window.get_root()
draw = Draw(canvas, root)
input_handler = Input(window.root)

def update(): #직접 업뎃 함수 정의
    draw.clear()

    draw.draw_text(canvas, 50, 50, "sans", size=24, color="black")

    window.update()

engine = GameEngine(update_func=update, fps=60)
engine.start()
