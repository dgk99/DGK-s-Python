# 삼각형 유형 판별 프로그램

# 사용자가 입력한 세 개의 수를 변의 길이로 하는 삼각형이 형성될수 있는지, 그리고 가능하다면 어떤 유형의 삼각형인지 판별합니다.
# 삼각형을 판별하기 위한 기준은 다음과 같습니다.



# 만약 세 변의 길이가 모두 다르다면, '부등변삼각형'입니다.
# 만약 어느 두 변의 길이 합이 나머지 한 변의 길이보다 작거나 같다면, 삼각형을 형성할수없습니다.

# 사용자에게 세 변의 길이를 입력받는다
num1 = int(input("첫 번째 변의 길이를 입력하세요: "))
num2 = int(input("두 번째 변의 길이를 입력하세요: "))
num3 = int(input("세 번째 변의 길이를 입력하세요: "))
# 세 변의 길이가 삼각형을 형성할 수 있는지 판단한다.
# 삼각형을 형성할 수 있다면, 삼각형의 유형을 출력한다.

# 만약 세 변의 길이가 모두 같다면, '정삼각형'입니다.
if num1 == num2 == num3 :
    print(f"입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")

# 그렇지 못하다면, 왜 만들 수 없는지 출력한다.
elif num1 + num2 < num3 or num1 + num3 < num2 or num3 + num2 < num1 :
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.")
    print("삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")

# 만약 세 변 중 두 변의 길이가 같다면, '이등변삼각형'입니다.
elif num1 == num2 or num2 == num3 or num1 == num3 :
    print(f"입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")
# 만약 세 변의 길이가 모두 다르다면, '부등변삼각형'입니다.
elif num1 != num2 != num3 :
    print(f"입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")

