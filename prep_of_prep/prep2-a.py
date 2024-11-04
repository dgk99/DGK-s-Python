# 면적 단위 변환기

# 사용자가 제곱미터 단위로 입력한 토지의 면적을 평방피트(ft2)와 에이커(ac)단위로
# 변환해주는 프로그램을 작성하세요

# 1제곱미터 = 10.7639 평방피트
# 1에이커 = 4046.86 제곱미터



# 제공된 변환 공식을 사용하여 면적을 평방피트와 에이커로 변환합니다.

def convert_to_square_feet(square_meters):
    square_feet = square_meters * 10.7639
    return square_feet
    
def convert_to_acres(square_meters):
    acres = square_meters / 4046.86
    return acres

# 사용자로부터 토지의 면적을 제곱미터 단위로 입력받습니다.
sm = float(input("토지의 면적을 제곱미터(m2) 단위로 입력하세요: "))

if sm < 0 : 
    print("잘못된 입력입니다")
else:
    print(float(sm),"제곱미터는",convert_to_square_feet(sm),"평방피트입니다.")
    print(float(sm),"제곱미터는",convert_to_acres(sm),"에이커입니다.")