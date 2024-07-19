# import pygame

# ## <<--- 초기화
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# ## --->>

# count = 0 # 생성되는 이미지 숫자를 의미
# ## <<--- 메인 루프
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     count += 1
    
#     print(count)
# ## --->> 이미지 생성


# ## 게임 종료
# pygame.quit()
# # ----------------------------------------------------
# import pygame

# ## <<--- 초기화
# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# ## <<--- fps 적용을 위한 시간 객체 설정
# clock = pygame.time.Clock() 
# fps = 0.5
# count = 0
# ## --->>

# ## <<--- 메인 루프
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
    
#     ## <<--- pygame fps 설정
#     print(count)
#     count += 1
#     clock.tick(fps)
# ## --->> 이미지 생성


# ## 게임 종료
# pygame.quit()
# # ----------------------------------------------------
# import pygame

# ## <<--- 초기화
# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# ## <<--- fps 적용을 위한 시간 객체 설정
# clock = pygame.time.Clock() 
# fps = 60
# radius = 40
# ## --->>

# x = screen.get_width()/2
# y = screen.get_height()/2
# speed = 100 # FPS 30 -> 300 pixel/second : speed 10 X 30번/초
#            # FPS 60 -> 600 pixel/second : speed 10 X 60번/초

# ## <<--- 메인 루프
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     dt = clock.tick(fps) / 1000.0
    
#     screen.fill((255, 255, 255))
    
#     pygame.draw.circle(screen, (255, 0, 0), (x, y),  40)
#     x += speed * dt
    
#     if x + radius >= screen.get_width() or x - radius <= 0:
#         speed = -speed
    
#     pygame.display.flip()
    
#     ## <<--- pygame fps 설정
#     clock.tick(fps)
# ## --->> 이미지 생성

# ## 게임 종료
# pygame.quit()
# # ----------------------------------------------------
import pygame

# Pygame 초기화
pygame.init()

# 화면 설정: 800픽셀 너비, 600픽셀 높이의 게임 화면을 생성
screen = pygame.display.set_mode((800, 600))

# 시계 객체 생성: 프레임 레이트 관리와 시간 계산을 위한 객체
clock = pygame.time.Clock()

# 원의 초기 위치: 화면 중앙
x = screen.get_width() / 2
y = screen.get_height() / 2
radius = 40 # 원의 반지름 설정

fps = 60

# 원의 이동 속도: 초당 100픽셀
speed = 500 # speed = pixel/second

# 게임 루프: 게임이 실행되는 동안 반복
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 델타 타임 계산: 마지막 프레임 이후 경과 시간을 초 단위로 변환
    # 이 값은 각 프레임 간의 시간차이로, 게임의 모든 시간 기반 계산에 사용
    dt = clock.tick(fps) / 1000.0 # FPS를 30으로 고정, 결과는 초 단위
    
    # 화면 지우기: 전체 화면을 검은색으로 채움
    screen.fill((0, 0, 0))
    
    # 원 그리기: 화면에 빨간색 원을 현재 x, y 위치에 그림
    pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)
    
    # 원 위치 업데이트: 속도와 델타 타임을 곱하여 이동 거리 계산
    x += speed * dt
    
    # 경계 처리: 원이 화면 가장자리에 닿으면 방향 전환
    if x - radius <= 0 or x + radius >= screen.get_width():
        speed = -speed
        
    # 화면 업데이트: 변경 사항을 화면에 반영
    pygame.display.flip()
    
    
# Pygame 종료 처리: 게임 루프 종료 후 Pygame 라이브러리 종료
pygame.quit()