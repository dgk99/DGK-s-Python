# 빙고 게임

# 입력 받기
import random

# 랜덤넘버 리스트의 인덱스를 나타내는 카운트

def make_bingo():
    a_count = 0
    for _ in range(num_input):
        for _ in range(num_input):
            print(random_num_list[a_count],end=" ")
            a_count += 1
            if a_count % 3 == 0:
                print()
    print()

# while True:
#     # 사용자로부터 크기 N을 일벽받는다. N은 3 이상 6 이하의 정수여야 한다
#     num_input = int(input("Enter the size of the bingo board (3 to 6): "))
#     # 유효하지 않은 값이 입력될 경우, 올바른 값이 입력될 때까지 재입력
#     if 3 > num_input or 6 < num_input:
#         print("Size must be between 3 and 6. Please try again.")
#     else:

num_input = 4
        
# 빙고 보드 생성
# N X N 크기의 빙고 보드를 위해 1차원 리스트를 생성
# 이 리스트는 1부터 36 사이의 중복되지 않은 정수로 채워진다
num_list = [int(value) for value in range(1, 37)]
# print(num_list)

# 보드 출력
# 랜덤으로 가져온 숫자가 저장될 리스트
random_num_list = []
# 생성된 리스트 중에서 빙고의 크기에 맞게 랜덤하게 가져온다
# 생성된 리스트를 사용하여 N X N 형태의 빙고 보드를 출력한다
# 리스트에 들어갈 값을 나타내는 카운트
# 반복해야 하는 횟수
cycle_num = num_input * num_input
while len(random_num_list) < cycle_num:

    random_num = num_list[random.randint(0, len(num_list) - 1)]
                        
    for j in random_num_list:
        if random_num == j:
            break
    else:
        random_num_list.append(random_num)

        
# 난수 발생 및 게임 진행
print("Initial Bingo Board:")
make_bingo()

# 정답용과 출력용 구분
printed_list = random_num_list[:]
        
 # 시도 횟수
game_count = 1

# 가로, 세로, 대각선 카운트
weight = 0
high = 0
cross = 0
# 빙고 카운트
weight_bingo = 0
high_bingo = 0
cross_bingo = 0


# 별이 몇개 생성 되었나 세는 카운트
star_count = 0
while True:
    

    # 사용자가 엔터키를 누르면, 1부터 36사이 난수를 발생시키고 화면에 출력한다
    print("Press Enter to generate a random number: ")
    correct_input = int(input(f"Random Number {game_count}: "))
    # 화면에 출력된 난수와 일치하는 보드 상의 숫자는 *로 대체된다
    if correct_input in random_num_list:
        for v in range(cycle_num):
            if correct_input == random_num_list[v]:
                random_num_list[v] = "*"
                star_count += 1
        make_bingo()
    game_count += 1
    # 매 난수 발생 시 게임 실행 횟수를 출력
    
    # 별을 나타내는 변수
    star = "*"
    
    # 빙고 확인
    # 보드에서 가로, 세로, 대각선(양방향)을 포함하여, 최소 2개 이상의 줄에서 모든 숫자가 *로 대체되면 빙고가 성립된다
    for g in range(cycle_num):
        for p in range(cycle_num):
            if random_num_list[g] != printed_list[p]:
                if g == p:
                    weight += 1
                if weight % 3 == 0:
                    weight_bingo += 1
                elif g != p:
                    high += 1
                if high % 3 == 0:
                    high_bingo += 1
    
    # 2개 이상의 빙고 줄이 완성되면 사용자가 승리
    if weight_bingo == 2 or high_bingo == 2 or cross_bingo == 2:
        print("Congratuaitons! You've won the game with 2 or more bingos!")
        break