from test import GameWindow
from test import Input
import time

win = GameWindow()
canvas = win.get_canvas()
input_handler = Input(win.get_root())

def main_loop():
    while True:
        canvas.delete("all")

        # 마우스 포인터 위치
        x, y = input_handler.get_mouse_pos()
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

        # 클릭 중이면 빨간 원
        if input_handler.is_mouse_pressed():
            canvas.create_oval(x-20, y-20, x+20, y+20, outline="red")

        # 키 입력 예시: 동시에 W, A 눌렀는지 체크
        keys = []
        if input_handler.is_key_pressed("w"):
            keys.append("W")
        if input_handler.is_key_pressed("a"):
            keys.append("A")
        if keys:
            canvas.create_text(100, 30, text="Keys: " + ",".join(keys), fill="green")

        win.update()
        time.sleep(1 / 60)

main_loop()
