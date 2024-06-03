# 문자열 내 단어 개수 출력

# for문을 사용하여 아래 문자열 내 단어 개수를 출력하는 프로그램 작성

myString = "It is a great weather with you"

myString_list = list(myString)

count = 1

for i in myString_list :
    if i == " " :
        count += 1
        
print("문자열 단어 갯수 : ", count)