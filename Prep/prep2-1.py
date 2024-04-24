3/27
'''
사용자가 제곱미터 단위로 입력한 토지의 면적을 평방피트와 에이커단위로 변환해주는 프로그램을 작성하세요.
1제곱미터 = 10.7639 평방피트
1에이커 = 4046.86 제곱미터
'''
# 제곱미터를 평방피트로 변환하는 코드
def convert_to_square_feet(square_meters):
    square_feet = square_meters * 10.7639
    return square_feet
# 제곱미터를 에이커로 변환하는 코드
def convert_to_acres(square_meters):
    acres = square_meters *  0.00024711
    return acres
# 사용자에게 제곱미터를 입력받는다
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))
# 만약 입력된 값이 0 보다 클 경우, 평방피트와 에이커를 계산한 값을 넣어 출력한다
if square_meters > 0 :
    print(square_meters,"제곱미터는" ,convert_to_square_feet(square_meters),"평방피트입니다.")
    print(square_meters,"제곱미터는" ,convert_to_acres(square_meters),"에이커입니다.")
    
# 만약 입력된 값이 0 보다 클 경우, 평방피트와 에이커를 계산한 값을 넣어 출력한다
elif square_meters < 0 :
    print("잘못된 입력입니다.")
