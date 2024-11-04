# 사칙연산 계산기

# 사용자에게 초기값을 입력받아 전역 변수로 선언합니다
baseValue = float(input("기본값을 입력하세요: "))

p = print("1. 더하기")
m = print("2. 빼기")
multi = print("3. 곱하기")
div = print("4. 나누기")

choose = int(input("선택: "))
putnum = int(input("숫자 입력: "))

# 프로그램은 사칙연산 중 하나의 연산을 수행할 수 있습니다.
# 사용자가 연산을 선택하고 숫자를 입력하면, selectOperation() 함수에서 선택한 연산을 baseValue에 적용합니다.
def selectOperation():
    # selecOperation()함수는 전역변수 baseValue를 참조하여 연산을 실행합니다.
    global baseValue
    
    if choose == 1 :
        baseValue = baseValue + putnum
    
    elif choose == 2 :
        baseValue = baseValue - putnum
    
    elif choose == 3 :
        baseValue = baseValue * putnum
    
    elif putnum == 0 :
        print("에러: 0으로 나눌 수 없습니다.") 
        return
    elif choose == 4 :
        baseValue = baseValue / putnum
    
    print("연산 결과: ", baseValue)

selectOperation()


# 나누기 연산에서 분모가 0 일 경우, "에러: 0으로 나눌 수 없습니다." 메시지 출력
# 에러 메시지가 출력되지 않은 경우에만, 연산 결과를 출력합니다.