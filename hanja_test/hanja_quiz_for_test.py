import pygame
import random
import csv
import re

# CSV 데이터를 로드
def load_questions_from_csv(file_path):
    questions = []
    all_kanji = set()  # 모든 한자를 저장할 집합
    with open(csv_file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "meaning" in row and "answer" in row and "characters" in row:
                kanji, hiragana = row["answer"].split(":")
                all_kanji.update(row.get("characters", "").split(","))  # 모든 한자를 집합에 추가
                questions.append({
                    "meaning": row["meaning"],
                    "kanji": kanji,  # 정답 전체 (한자 + 히라가나)
                    "hiragana": hiragana
                })
    return questions, sorted(all_kanji)  # 고유 한자 정렬 후 반환

# 파일 경로
csv_file_path = "hanja_hiragana_test.csv"
questions, all_kanji = load_questions_from_csv(csv_file_path)

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 1200, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hanja Quiz")

# 폰트 설정
font_path = "NotoSerifCJKjp-Regular.otf"
font = pygame.font.Font(font_path, 40)
small_font = pygame.font.Font(font_path, 25)

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)

# 문제 로드 함수
def load_new_question():
    question = random.choice(questions)
    # 한자만 추출 (히라가나 및 다른 문자는 그대로 둠)
    kanji_only = ''.join([char for char in question["kanji"] if re.match(r'[\u4e00-\u9fff]', char)])  # 한자 범위 유니코드 사용
    # 한자만 빈칸으로 변경 (히라가나는 유지)
    display_text = ''.join(["ㅁ" if re.match(r'[\u4e00-\u9fff]', char) else char for char in question["kanji"]])
    return question, list(kanji_only), display_text

# 게임 데이터
current_question, correct_kanji, display_text = load_new_question()
user_answer = [""] * len(correct_kanji)  # 정답 빈칸 초기화
feedback = ""
show_feedback_timer = 0  # 피드백 타이머
show_feedback = False

# 한자 보기 크기
kanji_button_width, kanji_button_height = 60, 60
columns = 15
padding = 10
kanji_start_y = 100
kanji_end_y = kanji_start_y + (len(all_kanji) // columns + 1) * (kanji_button_height + padding)
answer_start_y = kanji_end_y + 50

# 게임 루프
running = True
while running:
    screen.fill(white)

    # 뜻 출력
    meaning_text = font.render(f"뜻: {current_question['meaning']}", True, black)
    screen.blit(meaning_text, (screen_width // 2 - meaning_text.get_width() // 2, 20))

    # 보기 출력
    buttons = []
    for i, choice in enumerate(all_kanji):
        x_start = (screen_width - (columns * (kanji_button_width + padding))) // 2
        x = x_start + (i % columns) * (kanji_button_width + padding)
        y = kanji_start_y + (i // columns) * (kanji_button_height + padding)
        button_position = (x, y, kanji_button_width, kanji_button_height)
        pygame.draw.rect(screen, gray, button_position)
        button_text = small_font.render(choice, True, black)
        screen.blit(button_text, (x + 10, y + 10))
        buttons.append((button_position, choice))

    # 정답 빈칸 및 히라가나 출력
    for i, char in enumerate(display_text):
        x_start = (screen_width - (len(display_text) * (kanji_button_width + padding))) // 2
        blank_position = (x_start + i * (kanji_button_width + padding), answer_start_y, kanji_button_width, kanji_button_height)
        if char == "ㅁ":  # 한자 빈칸
            pygame.draw.rect(screen, gray, blank_position)
            if user_answer[i]:
                blank_text = small_font.render(user_answer[i], True, black)
                screen.blit(blank_text, (blank_position[0] + 10, blank_position[1] + 10))
            buttons.append((blank_position, i))  # 정답 칸
        else:
            # 히라가나 출력
            blank_text = small_font.render(char, True, black)
            screen.blit(blank_text, (blank_position[0] + 10, blank_position[1] + 10))

    # 피드백 표시
    if show_feedback:
        feedback_text = small_font.render(feedback, True, green if feedback == "정답입니다!" else red)
        screen.blit(feedback_text, (screen_width // 2 - feedback_text.get_width() // 2, answer_start_y + 80))
        if feedback == "정답입니다!":
            # 히라가나만 표시
            hiragana_text = font.render(current_question["hiragana"], True, black)
            screen.blit(hiragana_text, (screen_width // 2 - hiragana_text.get_width() // 2, answer_start_y - 50))

        # 타이머로 피드백을 사라지게 하거나 다음 문제로 전환
        if pygame.time.get_ticks() - show_feedback_timer > 1000:  # 1초 후 피드백 제거
            if feedback == "정답입니다!":
                current_question, correct_kanji, display_text = load_new_question()
                user_answer = [""] * len(correct_kanji)
            feedback = ""
            show_feedback = False

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for button in buttons:
                button_position, value = button
                if (
                    button_position[0] <= x <= button_position[0] + button_position[2]
                    and button_position[1] <= y <= button_position[1] + button_position[3]
                ):
                    if isinstance(value, int):  # 정답 칸 클릭
                        user_answer[value] = ""  # 정답 삭제
                    elif value in correct_kanji:  # 보기에서 정답 클릭
                        for i in range(len(user_answer)):
                            if not user_answer[i]:  # 첫 번째 빈칸에 넣기
                                user_answer[i] = value
                                break
                        # 정답 확인
                        if "".join(user_answer) == "".join(correct_kanji):  # 한자만 비교
                            feedback = "정답입니다!"
                            show_feedback_timer = pygame.time.get_ticks()
                            show_feedback = True
                    else:
                        feedback = "틀렸습니다"
                        show_feedback_timer = pygame.time.get_ticks()
                        show_feedback = True

    pygame.display.flip()

pygame.quit()
