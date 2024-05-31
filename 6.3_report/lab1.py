# 삼각형 출력

# while문을 사용하여 아래와 같이 출력하는 프로그램 작성

# 세로 별 카운트 지정
star_length_count = 0
star_width_count = 0
# 세로 별 카운트가 5보다 적으면 별을 출력하다가, 그 이상이면 종료
while star_length_count <= 5 : 
    star = ""
    star_length_count +=1
    # 가로 별 카운트가 4보다 작을때는 별을 출력하다가, 그 이상이면 종료
    while star_width_count <= 4 :
        star += "*"
        print(star)
        star_width_count += 1