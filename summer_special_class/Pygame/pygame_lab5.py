# 키보드 방향키 입력으로 직선 그리기
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 무작위 색상 생성
COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 시작점 (화면 중앙)
center_x = int(screen.get_width() / 2)
center_y = int(screen.get_height() / 2)
pixel = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.line(screen, COLOR, (center_x, center_y), (center_x, center_y - pixel))
                center_y = center_y - pixel
            elif event.key == pygame.K_DOWN:
                pygame.draw.line(screen, COLOR, (center_x, center_y), (center_x, center_y + pixel))
                center_y = center_y + pixel
            elif event.key == pygame.K_LEFT:
                pygame.draw.line(screen, COLOR, (center_x, center_y), (center_x - pixel, center_y))
                center_x = center_x - pixel
            elif event.key == pygame.K_RIGHT:
                pygame.draw.line(screen, COLOR, (center_x, center_y), (center_x + pixel, center_y))
                center_x = center_x + pixel
                        
            # center_x = center_x + pixel
            # center_y = center_y + pixel
    pygame.display.flip()
    
pygame.quit()