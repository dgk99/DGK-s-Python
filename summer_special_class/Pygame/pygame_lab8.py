import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collec Items Game')

# 색상
RED = ((255, 0, 0))
BLUE = ((0, 0, 255))
YELLOW = ((255, 255, 0))
WHITE = ((255, 255, 255))

# 장애물 생성 함수
def create_obstacles(num_obstacles, size, screen_width, screen_height):
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            rect = pygame.rect(random.randint(0, screen_width - size), \
                               random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles): # 다른 장애물과 겹치지 않음
                obstacles.append(rect)
                break
    return obstacles
# 아이템 생성 함수


running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # 화면 출력
    pygame.display.flip()
    
# 종료
pygame.quit()