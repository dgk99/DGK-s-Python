# 학생 성적 관리 프로그램

# 학생 입력 데이터 갯수
data_num = 0
# 전체 학생 평균 값
total_avg = 0

def menu():
    print("=" * 26)
    print("1. 학생 성적 입력\n2. 학생 목록 출력(입력 순)\n3. 프로그램 종료\n")
    print(f"현 입력데이터 갯수: {data_num}")
    print(f"전체 학생 평균 값: {float(total_avg)}")
    print("=" * 26)

student_list = []

while True:    
    menu()
    menu_input = int(input())

    if menu_input == 1:
        id = input("학번을 입력하세요\n")
        name = input("이름을 입력하세요\n")
        kor = int(input("국어 성적을 입력하세요\n"))
        eng = int(input("영어 성적을 입력하세요\n"))
        math = int(input("수학 성적을 입력하세요\n"))
        
        data_num += 1
        
        # 성적 합계
        sum = kor + eng + math
        
        # 성적 평균
        avg = sum / 3
        
        # 학생 정보 리스트에 저장
        student_list.append([id, name, kor, eng, math, sum, avg])
        
        # 전체 평균
        if data_num == 1:
            total_avg = avg
        else:
            total_avg = int((total_avg + avg)) / int(data_num)
        
    elif menu_input == 2 :
        for index in range(data_num):
            print(f"[ id : {student_list[index][0]} name : {student_list[index][1]} kor : {student_list[index][2]} eng : {student_list[index][3]} math : {student_list[index][4]} sum : {student_list[index][5]} avg : {student_list[index][6]}]")
    elif menu_input == 3:
        print("프로그램 종료")
        break
    else:
        print("1 ~ 3사이의 값을 입력하세요")
    