import pygame
import random
# 초기화
pygame.init()

# -->> 게임환경 변수
screen_width = 1280
screen_height = 720

# 색깔 변수
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 폰트 설정
font = pygame.font.SysFont(None, 50)

# 메인화면
main_screen = pygame.image.load("main.png")
main_text = font.render("Press Spacebar to Start", True, WHITE)
main_text_rect = main_text.get_rect(center=(screen_width // 2, screen_height // 2))
main_switch = False

# 인게임 화면
in_game_screen = pygame.image.load("in_game2.png")
# 체력 아이콘
full_heart = pygame.image.load("full_heart.png")
# 내 카드 위치

# 카드 이미지 로드
# 이미지 리스트 초기화
b_imgs = []
r_imgs = []

# b1.png ~ b13.png 이미지 로드
for i in range(1, 14):
    b_imgs.append(pygame.image.load(f"b{i}.png"))
print(b_imgs)
# red1.png ~ red13.png 이미지 로드
for i in range(1, 14):
    r_imgs.append(pygame.image.load(f"r{i}.png"))
# Rect 리스트 생성 및 위치 설정
b_rects = []
red_rects = []

for img in b_imgs:
    rect = img.get_rect()
    rect.topleft = (b_card_x, b_card_y)
    b_rects.append(rect)

for img in r_imgs:
    rect = img.get_rect()
    rect.topleft = (r_card_x, r_card_y)
    red_rects.append(rect)

# <<---

screen = pygame.display.set_mode((screen_width, screen_height))
running = True
# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 키 입력 받기
    keys = pygame.key.get_pressed()
    
    # 스페이스바가 눌러졌을 때 게임 시작
    if keys[pygame.K_SPACE]:
        main_switch = True
    # esc가 눌러졌을 때 게임 종료
    elif keys[pygame.K_ESCAPE]:
        running = False
    
    # 메인화면 출력
    screen.blit(main_screen, (0, 0))
    # 메인화면 글자 출력
    screen.blit(main_text, main_text_rect)
    
    # 스페이스바가 눌렸다면,
    # 게임 화면으로 넘어가기
    if main_switch == True :
        # 인게임 화면 출력
        screen.blit(in_game_screen, (0, 0))
        # 하트 출력
        screen.blit(full_heart, (0, 0))
        screen.blit(full_heart, (75, 0))
        screen.blit(full_heart, (150, 0))
        
    
    # 게임화면 출력
    pygame.display.flip()

# 종료
pygame.quit()