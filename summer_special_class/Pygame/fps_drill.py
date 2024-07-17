# 파이게임 불러오기
import pygame

# 색상 설정
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
running = True

# 화면 중심 좌표, 반지름, 속도 설정
x = screen.get_width() / 2
y = screen.get_height() / 2
r = 40
speed = 5

clock = pygame.time.Clock()

while running:
    # event가 발생할 때 마다 queue에 저장하고, 
    # get()이 호출되면, 호출된 시점부터 마지막까지 
    # 저장된 event를 list형태로 저장
    # 그 event들을 for반복문에 넣어 차례대로 출력
    for event in pygame.event.get():
        # 실행창의 x버튼을 누르면, 게임 종료
        if event.type == pygame.QUIT:
            running = False
        # 나머지 조건문이 있다면 작성해주기
    
    # 화면을 흰 색으로 채우기
    screen.fill((255, 255, 255))
    
    # 화면에 공 띄우기
    pygame.draw.circle(screen, RED, (x, y), r)
    
    # 공을 오른쪽으로 움직이기
    # x좌표에 speed를 더하여 움직이게 하기
    x += speed
    
    # 공이 화면 끝에 닿으면 다시 되돌아 가는 명령어
    # 공의 중심이 아닌, 테두리가 화면 끝이 닿으면 반대로 가는 명령어
    if x + r >= screen.get_width() or x - r <= 0:
        speed = -speed
    
    # 메모리에 있는 부분들을 화면으로 출력해주는 명령어
    pygame.display.flip()
    
    # 컴퓨팅 파워에 상관없이, delay시켜 일정한 fps로 출력하기
    clock.tick(60)
    
# 파이게임 종료
pygame.quit()