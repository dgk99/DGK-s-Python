# 마우스 클릭으로 원 그리기
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        
        r = random.randint(1, 100)
        # color1 = random.randint(0, 255)
        # color2 = random.randint(0, 255)
        # color3 = random.randint(0, 255)
        # COLOR = ((color1, color2, color3))
        COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # 사용자가 x 버튼을 누르면 게임이 종료
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, COLOR, (event.pos), r)
            pygame.display.flip()
pygame.quit()