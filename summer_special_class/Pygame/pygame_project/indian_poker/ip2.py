import pygame
import random

# 초기화
pygame.init()

## -->>

# 화면 너비
screen_width = 800
screen_height = 600
# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
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
win_text = font.render("WIN", True, BLUE)
draw_text = font.render("DRAW", True, GREEN)
lose_text = font.render("LOSE", True, RED)

# 텍스트 위치
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
coin_rect = coin_text.get_rect(topleft=(coin_1_x, coin_1_y - 20))

# 배경, 인게임 이미지 로드
game_start_img = pygame.image.load("game_start_screen.png")
game_table_img = pygame.image.load("game_table.png")
img_x_y = (0, 0)

# 인게임 음악
ingame_bgm = pygame.mixer.music.load("game_in_bgm.mp3")

b_imgs = []
red_imgs = []

# 카드 이미지 로드
for i in range(1, 14):
    b_imgs.append(pygame.image.load(f"b{i}.png"))
# red1.png ~ red13.png 이미지 로드
for i in range(1, 14):
    red_imgs.append(pygame.image.load(f"red{i}.png"))

# 카드 뒷면
back_img = pygame.image.load("back.png")
# 맥주 코인
coin_1_img = pygame.image.load("1coin.png")

# 게임 시작 플래그
game_started = False

# 상대 카드 랜덤 숫자
r_rand_num = random.randint(0, 12)
# 내 카드 랜덤 숫자
b_rand_num = random.randint(0, 12)

# 베팅 플래그
bet_flag = True
# 폴드 플래그
fold_flag = True

# 게임 리셋
def reset_game():
    global r_rand_num, b_rand_num, bet_flag, fold_flag, game_started
    r_rand_num = random.randint(0, 12)
    b_rand_num = random.randint(0, 12)
    bet_flag = True
    fold_flag = True
    game_started = False
## <<--

# 화면 설정
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

# 이벤트 처리
while running:
    # 종료 버튼을 누르면 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # 게임이 시작된 후 키 입력 이벤트 처리
        if event.type == pygame.KEYDOWN:
            # 스페이스바가 눌러졌을 때
            if event.key == pygame.K_SPACE:
                game_started = True
                pygame.mixer.music.play(fade_ms=1000)
            # esc가 눌러졌을 때
            elif event.key == pygame.K_ESCAPE:
                running = False
            # 왼쪽 화살표 키가 눌러졌을 때
            elif event.key == pygame.K_LEFT and game_started and coin_num > 0:
                coin_num -= 1
                bet_flag = False
            # 오른쪽 화살표 키가 눌러졌을 때
            elif event.key == pygame.K_RIGHT and game_started and coin_num > 0:
                coin_num -= 1
            
    # 게임 메뉴 화면
    if game_started == False:
        screen.blit(game_start_img, (img_x_y))
   
    # 게임이 시작되면
    elif game_started == True:
        # 인게임 화면 출력
        screen.blit(game_table_img, (img_x_y))

        # 코인 그리기
        coin_text = coin_font.render(f'{coin_num}EA', True, BLACK)
        coin_rect = coin_text.get_rect(topleft=(coin_1_x, coin_1_y - 20))
        screen.blit(coin_1_img, (coin_1_x, coin_1_y))
        screen.blit(coin_text, coin_rect)
        
        # 상대 카드 그리기
        enemy = screen.blit(red_imgs[r_rand_num], (r_card_x, r_card_y))
        
        # 내 카드 뒷면으로 씌워 놓기
        back = screen.blit(back_img, (b_card_x, b_card_y))
        
        # 베팅과 폴드 묻기
        if bet_flag:
            ask = screen.blit(text, text_rect)
        
        # 베팅을 했다면
        if not bet_flag:
            # 내 카드 그리기
            mine = screen.blit(b_imgs[b_rand_num], (b_card_x, b_card_y))
            
            pygame.time.wait(2000)
            
            # 내 카드와 상대 카드 비교
            if b_rand_num > r_rand_num:

                screen.blit(win_text, text_rect)
                coin_num + 2 
                coin_text = coin_font.render(f'{coin_num}EA', True, BLACK)
                
                reset_game()
            elif b_rand_num == r_rand_num:
                coin_num + 1
                screen.blit(draw_text, text_rect)
                coin_text = coin_font.render(f'{coin_num}EA', True, BLACK)
                
                reset_game()
            else:
                screen.blit(lose_text, text_rect)
                
                reset_game()
        elif not fold_flag: # 폴드를 했다면
            reset_game()
        
    # 화면 출력
    pygame.display.flip()
        
# 종료
pygame.quit()