def calculate_average(mat, sci, eng):
    average = ((mat + sci + eng) / 3)
    return average

def calculate_grade(average):   
    if average >= 90:
        grade = 'A'
    elif 90 > average >= 80:
        grade = 'B'
    elif 80 > average >= 70:
        grade = 'C'
    elif 70 > average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
        
mat = int(input("수학 점수를 입력하세요: "))
sci = int(input("과학 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))

average=calculate_average(mat, sci, eng)
grade = calculate_grade(average)

print("평균 점수는",average ,"이고, 학점은",grade,"입니다.")