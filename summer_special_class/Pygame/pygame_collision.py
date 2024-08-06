import pygame
# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rectangle Collision Example")

# 색상
RED = ((255, 0, 0))
BLACK = ((0, 0, 0))
BLUE = ((0, 0, 255))

# 사각형 초기화
rect1 = pygame.Rect(300, 220, 60, 60) # (300, 220) 위치에 60x60 크기의 사각형
rect2 = pygame.Rect(100, 100, 60, 60) # (100, 100) 위치에 60x60 크기의 사각형
rect1_speed = [10, 10] # rect1의 속도 (x 방향, y 방향)
rect2_speed = [5, 5] # rect2의 속도 (x 방향, y 방향)

# fps 설정
fps = 30
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(fps) # 설정된 fps에 따라 루프를 진행
    
    # 사각형 움직임
    rect1 = rect1.move(rect1_speed) # rect1을 속도만큼 이동
    rect2 = rect2.move(rect2_speed) # rect2을 속도만큼 이동

# 종료
pygame.quit()