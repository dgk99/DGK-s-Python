# 교수님이 만들어 주신 원 좌우로 움직이기
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

x = screen.get_width()/2
y = screen.get_height()/2
radius = 40

speed = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():     
        # 사용자가 x 버튼을 누르면 게임이 종료
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
    
    # 원 그리기
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)
    
    # 원의 x좌표를 + 방향으로 움직이게 함
    x += speed
    
    # 만약, 원의 테두리가 오른쪽 화면의 테두리(799, 0) 또는 그 반대(-799, 0)에 닿았다면,
    if x + radius >= screen.get_width() or x - radius <= 0:
        # 
        speed = -speed
       
    pygame.display.flip()
    
    clock.tick(60) # delay
    
pygame.quit()