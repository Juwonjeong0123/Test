class Input:
    def __init__(self, root):
        self.pressed_keys = set()
        self.mouse_pos = (0, 0)
        self.mouse_pressed = False

        root.bind("<KeyPress>", self._on_key_down) #이벤트명, 연결함수
        root.bind("<KeyRelease>", self._on_key_up)
        root.bind("<Motion>", self._on_mouse_move)
        root.bind("<ButtonPress>", self._on_mouse_down)
        root.bind("<ButtonRelease>", self._on_mouse_up)

    def _on_key_down(self, event):
        self.pressed_keys.add(event.keysym) #_키가 눌러졌을 때 호출, keysym은 눌러진 키, pressed_keys set에 추가

    def _on_key_up(self, event):
        self.pressed_keys.discard(event.keysym) #_키가 떼어졌을 때 호출, keysym은 떼어진 키, pressed_keys set에서 제거

    def is_key_pressed(self, key):
        return key in self.pressed_keys #pressed_keys set에 포함되어 있으면 True를 반환하고, 아니면 False를 반환합니다.
    
    def qwer(self):
        return #tlqkf
    
    def _on_mouse_move(self, event):
        self.mouse_pos = (event.x, event.y)

    def _on_mouse_down(self, event):
        self.mouse_pressed = True

    def _on_mouse_up(self, event):
        self.mouse_pressed = False

    def get_mouse_pos(self):
        return self.mouse_pos

    def is_mouse_pressed(self):
        return self.mouse_pressed

#https://076923.github.io/posts/Python-tkinter-23/#bind-event 바인드 이벤트 모음