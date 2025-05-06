import tkinter as tk

class GameWindow:
    def __init__(self, width=640, height=480, title="My Game"): #대충 매개변수 기본값 게이
        self.root = tk.Tk() #루트게이 = 트킨터
        self.root.title(title) #트킨터.타이틀 함수 실행
        self.canvas = tk.Canvas(self.root, width=width, height=height) #매개변수로 받은걸 트킨터 함수의 인자로 넘김
        self.canvas.pack() #함수
        self.width = width #가로
        self.height = height #세로

    def update(self):
        self.root.update_idletasks()
        self.root.update() #트킨터.업뎃

    def get_canvas(self):
        return self.canvas #캔버스 얻다

    def get_root(self):
        return self.root
