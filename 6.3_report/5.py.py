# 성적의 총합, 평균, 학생 수 출력 프로그램

# for문을 사용하여 아래 학생들의 성적에 대한 
# 총합, 평균, 학생 수를 출력하는 프로그램 작성하기

score = [99, 29, 30, 40, 20, 60]

# student_num = len(score)
student_num = 0
sum = 0
for s in score :
    sum += s
    student_num += 1

avg = sum / 6

print("학생 수 : ", student_num, ", 총점 : ", sum, ", 평균 : ", avg)