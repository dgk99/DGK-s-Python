# 학생 성적 관리 프로그램
# dictionary를 이용해 학생 성적 관리 프로그램을 작성

# 현 입력 데이터 갯수 카운트
data_num_count = 0
# 전체 학생 평균 값
avg_result = 0

# value값 저장할 리스트
value_list = []

# 메뉴 출력 함수
def menu():
    print("=" * 20)
    print(f"1. 학생 성적 입력\n2. 학생 목록 출력(입력 순)\n3. 프로그램 종료\n\n현 입력데이터 갯수 : {data_num_count}\n전체 학생 평균 값 : {float(avg_result)}")
    print("=" * 20)

# 학생 성적 입력 함수
def menu1():
    id = input("학번을 입력하세요\n")
    name = input("이름을 입력하세요\n")
    kor = int(input("국어 성적을 입력하세요\n"))
    eng = int(input("영어 성적을 입력하세요\n"))
    math = int(input("수학 성적을 입력하세요\n"))
    # 모든 성적의 합계
    sum = kor + eng + math
    # 성적의 평균
    avg = sum / 3


while True:
    menu()
    menu_input = int(input())

    if menu_input == 1:
        menu1()
        data_num_count += 1
    elif menu_input == 2:
        pass
    elif menu_input == 3:
        print("프로그램 종료")
        break
    else:
        print("1부터 3 사이의 값을 입력하세요")
        
# my_dict = dict(zip(key_list, value_list))
# print(my_dict)
