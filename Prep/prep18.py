# 점수 분류 및 평균 계산

# 학생들의 점수 리스트가 주어졌을 때, 각 점수를 분류하고 분류된 점수들의 평균을 계산

# 90점 이상 = '우수'
# 70점 이상 90점 미만 = '양호'
# 50점 이상 70점 미만 = '보통'
# 50점 미만 = '미흡'

# 각 분류에 따른 점수의 평균을 계산하고, 분류된 점수 리스트와 각 분류의 평균 점수를 출력

# 학생들의 점수 리스트
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

score_over_90 = [value for value in scores if value >= 90]
score_over_70 = [value for value in scores if 70 <= value < 90]
score_over_50 = [value for value in scores if 50 <= value < 70]
score_under_50 = [value for value in scores if value <= 50]

sum1 = 0
for avg in score_over_90 :
    sum1 += avg
    score_avg_90 = sum1 / len(score_over_90)
    
sum2 = 0
for avg in score_over_70 :
    sum2 += avg
    score_avg_70 = sum2 / len(score_over_70)
    
sum3 = 0
for avg in score_over_50 :
    sum3 += avg
    score_avg_50 = sum3 / len(score_over_50)
    
sum4 = 0
for avg in score_under_50 :
    sum4 += avg
    score_avg_50under = sum4 / len(score_under_50)
    
print(f"우수: {score_over_90} 평균: {score_avg_90}")
print(f"양호: {score_over_70} 평균: {score_avg_70}")
print(f"보통: {score_over_50} 평균: {score_avg_50}")
print(f"미흡: {score_under_50} 평균: {score_avg_50under}")