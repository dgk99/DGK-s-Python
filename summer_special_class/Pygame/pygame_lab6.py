import pygame
import random

# 초기화
pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True

# 화면 중앙
x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 30

# 색상
RED = ((255, 0, 0))
BLACK = ((0, 0, 0))
YELLOW = ((255, 255, 0))
GREEN = ((0, 255, 0))
BLUE = ((0, 0, 255))
color_list = [RED, BLACK, YELLOW, GREEN, BLUE]
rand_color = random.randint(0, 4)


# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, color_list[rand_color], (x, y), radius)

    pygame.display.flip()
# 종료
pygame.quit()