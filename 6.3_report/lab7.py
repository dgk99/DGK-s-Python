# 별 다이아몬드 출력

# 높이가 5인 다이아몬드 형태의 별 출력
black_width_count = 5
star_length_count = 2
# 공백 세로 반복문
for b1 in range(1, 6) :
    blank = ""
    # 공백 가로 반복문
    for b2 in range(1, black_width_count) :
        blank += " "
    black_width_count -= 1
    # 별 세로 반복문
    for s1 in range(1, star_length_count) :
        blank += "*"
    star_length_count += 2
    print(blank)
    
# 역 공백 세로 반복문
re_blank_length_count = 2
re_star_width_count = 8
for b3 in range(1, 5) :
    blank3 = ""
    for b4 in range(1, re_blank_length_count) : 
        blank3 += " "
    re_blank_length_count += 1
    for s2 in range(1, re_star_width_count) :
        blank3 += "*"
    re_star_width_count -= 2
    print(blank3)