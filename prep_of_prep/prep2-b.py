# 평균 점수와 학점 등급 계산 프로그램

# 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램 만들기


# 입력받은 점수들을 바탕으로 평균 점수를 계산합니다.
# 계산된 평균 점수를 사용하여 학점 등급을 결정합니다.
def calculate_average(math, sci, eng):
    plus = math + sci + eng
    div = plus / 3
    return div

def calculate_grade(div):
    if div > 90 :
        grade = "A"
    elif 90 > div >= 80:
        grade = "B"
    elif 80 > div >= 70:
        grade = "C"
    elif 70 > div >= 60:
        grade = "D"
    elif 60 > div:
        grade = "F"
    return grade
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만

# 사용자로부터 수학, 과학, 영어의 점수를 입력받습니다.
math = float(input("수학 점수를 입력하세요: "))
sci = float(input("과학 점수를 입력하세요: "))
eng = float(input("영어 점수를 입력하세요: "))

ave = calculate_average(math, sci, eng)
div = calculate_grade(ave)

print("평균 점수는",ave,"점이고, 학점은",div,"입니다.")