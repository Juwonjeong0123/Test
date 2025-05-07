class Sprite:
    def __init__(self, x, y, width, height, color="black", speed=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def update(self, vec):
        self.x += vec.x * self.speed
        self.y += vec.y * self.speed

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x, self.y,
            self.x + self.width, self.y + self.height,
            fill=self.color
        )

    def get_rect(self):
        return (self.x, self.y, self.x + self.width, self.y + self.height)


# 위치, 이미지, 이동 속성 보유
# 일단 이동 함수, 이미지를 생성자 함수 매개변수로
# 1. dir 매개변수 하나만 받기 <- ㅈㅁ 이거 Vector로 받으면 되는거 아닌가 시발 난 천재다 으하하하하하하하하하하하하하하
# 2. x y 따로 받기
# 일단 move의 매개변수 타입은 Vector인데 시발 이걸 어케 구현함
# 오 시발 벡터를 받고 함수 내부에서 벡터.x 벡터.y 이따구로 하면 되네 시발 으하하하하화하하핳하하하하하하하핳하하
# 스프라이트 파일이 가로 세로 30대 1이거나 60대 1인걸 나눠서 프레임별로 이미지를 나누는 그런 함수 구현
# 매개변수에 이미지를 그냥 배열로 할까 스프라이트 파일로 할까
# 일단 선택사항으론 하다
# 애니는 어케 구현함 ㅅㅂ
# 시발 일단 간단하게 이동만 생각하자

class SpriteGroup:
    #여러 스프라이트 관리
    def gay():
        print("ㅗ")