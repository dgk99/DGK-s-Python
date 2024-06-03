# 삼각형 출력

# while문을 사용하여 아래와 같이 출력하는 프로그램 작성

# 별 카운트
star_count = 0

star = ""
# 별 카운트가 4보다 적거나 같을 때 까지 실행하다가, 4와 같거나 4보다 크면 실행 종료
while star_count <= 4 :
    # 반복문이 실행될 때 마다 star에다가 * 추가
    star += "*"
    print(star)
    star_count += 1