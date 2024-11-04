# import pygame
# # 초기화
# pygame.init()

# screen = pygame.display.set_mode((640, 480))
# running = True
# # 이벤트 처리
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         # for문 안쪽에 있을 경우
#         screen.fill((255, 255, 255)) # 이벤트가 발생할 때
#         pygame.display.flip()
        
#     # for문 바깥에 있을 경우
#     # 이벤트 처리가 끝난 후
#     screen.fill((255, 255, 255)) # 이벤트가 발생할 때
#     pygame.display.flip()
            
# # 종료
# pygame.quit()

# # 색상 정의
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# import pygame
# # 초기화
# pygame.init()

# screen = pygame.display.set_mode((640, 480))
# running = True
# # 이벤트 처리
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     pygame.draw.circle(screen, GREEN, (100, 200), 40)
#     pygame.draw.circle(screen, RED, (300, 500), 40)
    
#     screen.fill((255, 255, 255))
    
#     pygame.display.flip()

# # 종료
# pygame.quit()


# 색상 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

import pygame
# 초기화
pygame.init()


screen = pygame.display.set_mode((800, 600))

# 공의 x좌표
x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40
speed = 5

running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, RED, (x, y), radius)
    
    if x + radius >= screen.get_width() or x - radius <= 0:
        speed = -speed
        
    x += speed
    pygame.display.flip()

# 종료
pygame.quit()
