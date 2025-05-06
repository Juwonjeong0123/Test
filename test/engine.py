import time

class GameEngine:
    def __init__(self, update_func, fps=60): #매개변수로 업뎃 함수, fps 받기, 기본 fps=60
        self.update_func = update_func #사용자 입력 처리, 화면 갱신, 물리 연산 등 업뎃 함수
        self.fps = fps
        self.running = False

    def start(self):
        self.running = True
        frame_time = 1 / self.fps
        while self.running:
            start_time = time.time()

            self.update_func()

            elapsed = time.time() - start_time
            sleep_time = frame_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    def stop(self):
        self.running = False
