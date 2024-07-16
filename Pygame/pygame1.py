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