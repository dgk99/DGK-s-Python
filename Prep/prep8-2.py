# 사칙연산 계산기
# 사용자로부터 초기값을 입력받아 전역 변수로 선언합니다.
# 프로그램은 더하기, 빼기, 곱하기, 나누기 중 하나의 연산을 수행할 수 있습니다.
# 사용자가 연산을 선택하고 숫자를 입력하면, selectOperation() 함수에서 선택한 연산을 baseValue에 적용합니다.
# selectOperation() 함수는 전역 변수 baseValue를 참조하여 연산을 실행합니다.
# 나누기 연산에서 분모가 0일 경우, "에러: 0으로 나눌 수 없습니다."라는 메시지를 출력합니다.
# – 이 경우, 연산 결과는 출력하지 않습니다.
# 에러 메시지가 출력되지 않은 경우에만, 연산 결과를 출력합니다.

# 전역 변수 선언 및 사용자로부터 입력 받기
baseValue = float(input("기본값을 입력하세요: "))
p = print("1. 더하기")
m = print("2. 뺴기")
multi = print("3. 곱하기")
d = print("4. 나누기")

choice = int(input("선택 : "))
numberinput = int(input("숫자 입력: "))

def selectOperation():
    global baseValue
    
    if choice == 1:
        baseValue = baseValue + numberinput
    elif choice == 2:
        baseValue = baseValue - numberinput
    elif choice == 3:
        baseValue = baseValue * numberinput
    elif numberinput == 0 :
        print("에러: 0으로 나눌 수 없습니다.")
        return
    elif choice == 4:
        baseValue = baseValue / numberinput
    #if numberinput == 0 :
    #    print("에러: 0으로 나눌 수 없습니다.")
        
    
    print("연산결과: ", baseValue)
    
selectOperation()