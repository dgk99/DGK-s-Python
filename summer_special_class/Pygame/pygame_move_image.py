import pygame
# 초기화
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Image Movement")

# 색상 정의
white = (255, 255, 255)

# 이미지 로드
blue_image = pygame.image.load("blue_rect.png")
red_image = pygame.image.load("red_rect.png")

# 이미지 위치 초기 설정
blue_rect = blue_image.get_rect()
blue_rect.topleft = (100, 100)

red_rect = red_image.get_rect()
red_rect.topleft = (200, 200)

# 이동 속도
speed = 1

running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        blue_rect.x += speed
    if keys[pygame.K_UP]:
        blue_rect.y -= speed
    if keys[pygame.K_DOWN]:
        blue_rect.y += speed
    if keys[pygame.K_a]:
        red_rect.x -= speed
    if keys[pygame.K_d]:
        red_rect.x += speed
    if keys[pygame.K_w]:
        red_rect.y -= speed
    if keys[pygame.K_s]:
        red_rect.y += speed
        
    # 화면을 흰색으로 채우기
    screen.fill(white)
    
    # 이미지 그리기
    screen.blit(blue_image, blue_rect)
    screen.blit(red_image, red_rect)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
