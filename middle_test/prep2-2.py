# 평균 점수와 학점 등급 계산 프로그램

# 학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램을 만드시오

# 사용자로부터 수학,과학,영어의 점수를 입력받는다
math = int(input("수학 점수를 입력하세요: "))
sci = int(input("과학 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
# 입력받은 점수들을 바탕으로 평균 점수를 계산합니다.
# 계산된 평균 점수를 사용하여 학점 등급을 결정합니다.
# 학점 등급은 평균 점수에 따라 다음과 같이 할당됩니다.
def calculate_average(math, sci, eng):
    plus = math + sci + eng
    average = plus / 3
    if average >= 90 : # A : 90점 이상
        grade = "A"
    elif 80 <= average < 90 : # B : 80점 이상 90점 미만
        grade = "B"
    elif 70 <= average < 80 : # C : 70점 이상 80점 미만
        grade = "C"
    elif 60 <= average < 70 : # D : 60점 이상 70점 미만
        grade = "D"
    elif average < 60 : # E : 60점 미만
        grade = "E"
    return grade
    
average = (math + sci + eng)/3

# 각 과목의 점수와 함께 평균 점수 및 해당하는 학점 등급을 출력합니다.
print(f"평균 점수는 {average}점이고, 학점은 {calculate_average(math, sci, eng)}입니다.")