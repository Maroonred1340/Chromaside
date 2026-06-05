Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
```python
import pygame

# 게임 설정
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE_SKY = (135, 206, 235)
DARK_BLUE = (0, 0, 139)

# 플레이어 설정
PLAYER_SIZE = 50
PLAYER_SPEED = 5
GRAVITY = 0.5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity_y = 0
        self.direction = pygame.math.Vector2(0, 0) # 화살표 방향

    def update(self):
        # 중력 적용
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # 화면 밖으로 나가지 않도록 처리
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # 방향으로 이동
        if self.direction.length() > 0:
            self.direction.normalize_ip() # 벡터 정규화
            move_x = self.direction.x * PLAYER_SPEED
            move_y = self.direction.y * PLAYER_SPEED
            self.rect.x += move_x
            self.rect.y += move_y
            self.direction = pygame.math.Vector2(0, 0) # 이동 후 방향 초기화

    def move_in_direction(self, target_pos):
        # 클릭 위치를 기준으로 방향 설정
...         dx = target_pos[0] - self.rect.centerx
...         dy = target_pos[1] - self.rect.centery
...         self.direction = pygame.math.Vector2(dx, dy)
... 
... # Pygame 초기화
... pygame.init()
... screen = pygame.display.set_mode((WIDTH, HEIGHT))
... pygame.display.set_caption("화살표 게임")
... clock = pygame.time.Clock()
... 
... # 플레이어 생성
... player = Player()
... all_sprites = pygame.sprite.Group()
... all_sprites.add(player)
... 
... # 게임 루프
... running = True
... while running:
...     # 이벤트 처리
...     for event in pygame.event.get():
...         if event.type == pygame.QUIT:
...             running = False
...         elif event.type == pygame.MOUSEBUTTONDOWN:
...             if event.button == 1: # 왼쪽 클릭
...                 player.move_in_direction(event.pos)
... 
...     # 업데이트
...     all_sprites.update()
... 
...     # 그리기
...     screen.fill(WHITE) # 기본 배경색
...     # 파랑-하늘색 그라데이션 배경
...     for y in range(HEIGHT):
...         ratio = y / HEIGHT
...         color = [
...             BLUE_SKY[0] * (1 - ratio) + DARK_BLUE[0] * ratio,
...             BLUE_SKY[1] * (1 - ratio) + DARK_BLUE[1] * ratio,
...             BLUE_SKY[2] * (1 - ratio) + DARK_BLUE[2] * ratio
...         ]
...         pygame.draw.line(screen, color, (0, y), (WIDTH, y), 1)
... 
...     all_sprites.draw(screen)
... 
...     # 화면 업데이트
...     pygame.display.flip()
... 
...     # FPS 설정
...     clock.tick(FPS)
... 
... pygame.quit()
