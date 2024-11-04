import pygame
import random

# 초기화
pygame.init()

# -->>
# 배경음악 파일 로드
bgm_music = pygame.mixer.music.load("Hearthstone Main Theme.mp3")

# 배경음악 무한 반복 재생 시작
pygame.mixer.music.play(-1)

# 화면 너비
screen_width = 800
screen_height = 600
# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# 카드 크기
card_width = 50
card_height = 70

# 내 카드 위치
b_card_x = screen_width // 2 - card_width // 2
b_card_y = screen_height - 200
# 상대 카드 위치
r_card_x = screen_width // 2 - card_width // 2
r_card_y = screen_height - 450

# 맥주 코인 위치
coin_1_x = 180
coin_1_y = 380
coin_num = 10

# 폰트 설정
font = pygame.font.Font(None, 60)  # 기본 폰트를 크기 74로 설정
coin_font = pygame.font.Font(None, 30) # 코인용 폰트
# 텍스트 렌더링
text = font.render('<- Bet? or Fold? ->', True, WHITE)  # 흰색으로 텍스트 생성
coin_text = coin_font.render(f'{coin_num}EA', True, BLACK)
# 텍스트 위치
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
coin_rect = coin_text.get_rect(topleft=(coin_1_x, coin_1_y - 20))

# 화면 설정
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

# 카드 이미지 로드
# 이미지 리스트 초기화
b_imgs = []
red_imgs = []

# b1.png ~ b13.png 이미지 로드
for i in range(1, 14):
    b_imgs.append(pygame.image.load(f"b{i}.png"))
print(b_imgs)
# red1.png ~ red13.png 이미지 로드
for i in range(1, 14):
    red_imgs.append(pygame.image.load(f"red{i}.png"))

# 카드 뒷면
back_img = pygame.image.load("back.png")
# 맥주 코인
coin_1_img = pygame.image.load("1coin.png")
coin_1_rect = coin_1_x, coin_1_y

# 게임 초기 화면 로드
game_start_screen_img = pygame.image.load("game_start_screen.png")
game_start_screen_rect = (0, 0)
# 게임 테이블 화면 로드
game_table_img = pygame.image.load("game_table.png")
game_table_rect = (0, 0)

# Rect 리스트 생성 및 위치 설정
b_rects = []
red_rects = []

for img in b_imgs:
    rect = img.get_rect()
    rect.topleft = (b_card_x, b_card_y)
    b_rects.append(rect)

for img in red_imgs:
    rect = img.get_rect()
    rect.topleft = (r_card_x, r_card_y)
    red_rects.append(rect)

# 상대 카드 랜덤 숫자
r_rand_num = random.randint(0, 12)
# 내 카드 랜덤 숫자
b_rand_num = random.randint(0, 12)

# 게임이 시작하는지 확인하는 플래그
game_started = True

# 베팅을 하면 뒷면이 사라지는 플래그
remove_back = True

# <<--

# 이벤트 처리
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 키 입력 받기
    keys = pygame.key.get_pressed()   
    
    # 스페이스바가 눌러졌을 때
    if keys[pygame.K_SPACE]:
        game_started = False
    # esc가 눌러졌을 때
    elif keys[pygame.K_ESCAPE]:
        running = False

    if game_started == False:
        # 화면 테이블 그림으로 채우기
        screen.blit(game_table_img, game_table_rect)
        
        # 코인 그리기
        screen.blit(coin_1_img, coin_1_rect)
        screen.blit(coin_text, coin_rect)
        
        # 상대 카드 그리기
        screen.blit(red_imgs[r_rand_num], red_rects[r_rand_num])
        # 내 카드 그리기
        screen.blit(b_imgs[b_rand_num], b_rects[b_rand_num])
        # 내 카드 뒷면으로 씌워 놓기
        screen.blit(back_img, b_rects[b_rand_num])
        
        # 베팅과 폴드 묻기
        screen.blit(text, text_rect)
        
        # 베팅일 경우 묻는 문자, 뒷면 삭제
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                remove_back = False
                
        
        # 만약, 이겼을 경우, 상대 코인까지 가져오기
        if b_rand_num > r_rand_num:
            coin_num += 2
        # 만약 비겼을 경우, 코인 회수
        elif b_rand_num == r_rand_num:
            coin_num += 1
        # 졌을 경우는 냈던 코인 잃으면 돼서 지정하지 않아도 댐
        
    else:
        # 게임 시작 화면 그리기
        screen.blit(game_start_screen_img, game_start_screen_rect)
    
    # 화면 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
