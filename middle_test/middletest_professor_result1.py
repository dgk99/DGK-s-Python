
input_1 = int(input("1번째 값을 입력하세요: "))
input_2 = int(input("2번째 값을 입력하세요: "))
input_3 = int(input("3번째 값을 입력하세요: "))
input_4 = int(input("4번째 값을 입력하세요: "))
input_5 = int(input("5번째 값을 입력하세요: "))

sum = input_1 + input_2 + input_3 + input_4 + input_5

avg = sum / 5

print("합계 : ", sum)
print("평균 : ", avg)


# for 사용
for count in range(1, 6):
    msg = str(count) + "번째 입력하세요"
    input_value = int(input(msg))
    sum += input_value
    
avg = sum / 5

print("합계 : ", sum)
print("평균 : ", avg)