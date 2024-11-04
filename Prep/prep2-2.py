3/27
# 학생들의 세 과목 점수를 입력 받아 평균 점수를 계산하고, 평균에 따른 학점 등급을 부여하는 프로그램을 만드시오
# 사용자로부터 수학, 과학, 영어의 점수를 입력받는다
# 입력받은 점수들을 바탕으로 평균 점수를 계산한다.
# 계산된 평균 점수를 사용하여 학점 등급을 결정한다.
'''
a = 90점 이상
b = 80점 이상 90점 미만
c = 70점 이상 80점 미만
d = 60점 이상 70점 미만
f = 60점 미만'''

# 각 과목의 점수와 함께 평균 점수 및 해당하는 학점 등급을 출력합니다.
# 세 과목의 점수를 더하고 3으로 나눠 평균을 구한다
def calculate_average(math_score, science_score, english_score):
    score_average = (math_score + science_score + english_score) / 3
    return score_average
# 세 과목의 각각의 점수를 입력받는다.
math_score = float(input("수학 점수를 입력하세요: "))
science_score = float(input("과학 점수를 입력하세요: "))
english_score = float(input("영어 점수를 입력하세요: "))
# 세 과목의 평균값과 평균값에 알맞는 학점을 부과하여 출력한다.
if calculate_average(math_score, science_score, english_score) >= 90 :
    print("평균점수는",calculate_average(math_score, science_score, english_score),"점이고,","학점은 A입니다.")
elif 90 >= calculate_average(math_score, science_score, english_score) >= 80 :
    print("평균점수는",calculate_average(math_score, science_score, english_score),"점이고,","학점은 B입니다.")
elif 80 >= calculate_average(math_score, science_score, english_score) >= 70 :
    print("평균점수는",calculate_average(math_score, science_score, english_score),"점이고,","학점은 C입니다.")
elif 70 >= calculate_average(math_score, science_score, english_score) >= 60 :
    print("평균점수는",calculate_average(math_score, science_score, english_score),"점이고,","학점은 D입니다.")
elif 60 >= calculate_average(math_score, science_score, english_score) :
    print("평균점수는",calculate_average(math_score, science_score, english_score),"점이고,","학점은 F입니다.")
    
    