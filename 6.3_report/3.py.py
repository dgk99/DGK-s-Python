# 문자열 내 h 글자 개수 구하기

# for 문을 사용하여 아래 문자열 내 h의 개수를 출력하는 프로그램 작성

myString = "hello hyundai hoho"

myString_list = list(myString)

count = 0

for i in myString_list :
    if i == "h" :
        count += 1

print("문자열 내 h 갯수 : ", count)
    
    
