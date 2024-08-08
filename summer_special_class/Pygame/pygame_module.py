import pygame
# 초기화
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)
# 종료
pygame.quit()
# ----------------------------------------------------------
import pygame
# 초기화
pygame.init()

screen = pygame.display.set_mode((640, 480))
running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
# 종료
pygame.quit()
#----------------------------------------------------------------------
import pygame
# 초기화
pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 종료
pygame.quit()

# 색상
RED = ((255, 0, 0))
BLACK = ((0, 0, 0))
BLUE = ((0, 0, 255))
YELLOW = ((255, 255, 0))
GREEN = ((0, 255, 0))
WHITE = ((255, 255, 255))
