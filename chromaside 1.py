python
import tkinter as tk
import math

class Player:
    def init(self, canvas, x, y):
        self.canvas = canvas
        self.size = 50
        self.color = "green"
        self.rect = self.canvas.createrectangle(x - self.size // 2, y - self.size // 2, x + self.size // 2, y + self.size // 2, fill=self.color)
        self.velocityy = 0
        self.directionvector = (0, 0)  x, y 방향
        self.canvaswidth = canvas.winfowidth()
        self.canvasheight = canvas.winfoheight()

    def update(self):
         화면 크기 업데이트 (창 크기 변경 시)
        self.canvaswidth = self.canvas.winfowidth()
        self.canvasheight = self.canvas.winfoheight()

         중력 적용
        self.velocityy += 0.5
        self.canvas.move(self.rect, 0, self.velocityy)

         화면 밖으로 나가지 않도록 처리
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        if y1 < 0:
            self.canvas.coords(self.rect, x1, 0, x2, y2 - y1)
            self.velocityy = 0
        if y2 > self.canvasheight:
            self.canvas.coords(self.rect, x1, self.canvasheight - (y2 - y1), x2, self.canvasheight)
            self.velocityy = 0
        if x1 < 0:
            self.canvas.coords(self.rect, 0, y1, x2 - x1, y2)
        if x2 > self.canvaswidth:
            self.canvas.coords(self.rect, self.canvaswidth - (x2 - x1), y1, self.canvaswidth, y2)

         방향으로 이동
        if self.directionvector != (0, 0):
            movex = self.directionvector[0]  5
            movey = self.directionvector[1]  5
            self.canvas.move(self.rect, movex, movey)
            self.directionvector = (0, 0)  이동 후 방향 초기화

    def moveindirection(self, targetpos):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        centerx = (x1 + x2) / 2
        centery = (y1 + y2) / 2

        dx = targetpos[0] - centerx
        dy = targetpos[1] - centery

         벡터 정규화 (길이 1로 만들기)
        magnitude = math.sqrt(dx2 + dy2)
        if magnitude > 0:
            self.directionvector = (dx / magnitude, dy / magnitude)
        else:
            self.directionvector = (0, 0)

def updategame():
    player.update()
    window.after(16, updategame)  약 60 FPS

def onclick(event):
    player.moveindirection(event.x, event.y)

 Tkinter 윈도우 설정
window = tk.Tk()
window.title("화살표 게임 (Tkinter)")
window.geometry("800x600")

 캔버스 생성
canvas = tk.Canvas(window, width=800, height=600, bg="skyblue")
canvas.pack()

 플레이어 생성
player = Player(canvas, 400, 300)

 마우스 클릭 이벤트 바인딩
canvas.bind("<Button-1>", onclick)

 게임 루프 시작
updategame()

 윈도우 실행
window.mainloop()
