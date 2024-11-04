import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
pygame.display.flip()

# 원의 갯수
num = random.randint(5, 20)

for i in range(num):
    # 가로 좌표, 세로 좌표, 반지름, 무작위 색 랜덤 생성
    x = random.randint(0, 799)
    y = random.randint(0, 599)
    r = random.randint(1, 100)
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    COLOR = (color1, color2, color3)

    # 원 그리기
    pygame.draw.circle(screen, COLOR, (x, y), r)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()