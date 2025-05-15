class GameEngine:
    def __init__(self, root, update_func, fps=60): #매개변수로 업뎃 함수, fps 받기, 기본 fps=60
        self.update_func = update_func #사용자 입력 처리, 화면 갱신, 물리 연산 등 업뎃 함수
        self.fps = fps
        self.running = False
        self.root = root

    def start(self):
        self.running = True
        self._loop()
        self.root.mainloop()

    def _loop(self):
        if self.running:
            self.update_func()
            self.root.after(int(1000 / self.fps), self._loop)

    def stop(self):
        self.running = False
        self.root.quit()
