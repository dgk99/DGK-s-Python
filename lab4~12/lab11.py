# 사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하는 함수를 작성하고, 변환된 화씨를 출력하는 프로그램을 만드시오
# 사용자에게 섭씨 온도를 입력받으시오.
cel = int(input("섭씨 온도를 입력하세요: "))

# 입력받은 섭씨 온도를 화씨 온도로 변환한다.
# 화씨 온도 F=(C*9/5)+32

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

print("화씨 온도는",convert_celsius_to_fahrenheit(cel),"입니다.")
