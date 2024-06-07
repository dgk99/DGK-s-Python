# 주민번호 유효성 검사

# 주민번호는 총 13자리

# 예시 주민번호 = 790608-2552416

# 사용자로부터 문자열 입력받기
text = list(input("문자열을 입력하세요: "))
# 입력받은 문자열에서 - 빼기. list는 .remove 함수 사용
text.remove("-")
# 주민번호의 앞 12자리를 각각 2,3,4,5,6,7,8,9,2,3,4,5로 곱한다
# 곱해야 하는 수를 리스트로 만들어준다
check_num = [2,3,4,5,6,7,8,9,2,3,4,5]
# 검사해야하는 주민번호는 12자리니까 count를 만들어주고, count가 12면 = 검사해야할 수가 12자리 까지 오면 break하기
count = 0
# 각 수를 곱한 값을 다 더해줘야 하니 sum이라는 변수 만들어주기
sum = 0
for i in text: # 입력값을 i로 하나씩 넣어주기
    if count != 12: # count가 12가 되기 전까지 => 12가 되면 바로 종료
        sum += int(i) * check_num[count] # sum에다 i * check_num의 index 0부터 12까지 곱해주기
        count += 1 # 곱해줄 때 마다 count에다 더하기 1
        
# for i in range(12):
#     sum += int(text[i]) * int(check_num[i])


# 이 결과를 모두 더한다
# 더한 결과를 11로 나눈 나머지를 구한다
divison = sum % 11
# 11에서 이 나머지를 뺀다
num = 11 - divison
# 결과가 두 자리일 경우, 10 자리는 버리고 1 자리만 사용
if num > 10 :
    result = num % 10
else:
    result = num

if result == int(text[-1]):
    print("검증번호와 나머지가 일치! 정답~~")
else:
    print("실패야")
# 최종 결과가 마지막 숫자와 일치하면 유효한 주민번호