#나이를 입력받습니다(정수형)
age = int(input("나이를 입력하세요: "))
#입력된 나이에 따라 청소년(Teenager), 성인(Adult), 노년(Senior)중 하나로 분류합니다
#13~19세 사이는 청소년(Teenager)
if 19 >= age >= 13:
    print("You are in the 'Teenager' age group")
#20~64세 사이는 성인(Adult)
elif 64 >= age >= 20:
    print("You are in the 'Adult' age group")
#65세 이상은 노년(Senior)
elif 65 <= age:
    print("You are in the 'Senior' age group")
#해당하는 나이대의 영어단어를 출력합니다
#범위에 맞지않는 입력값에 대해서는 "Unknown age group"이라고 출력합니다
else:
    print("You are in the 'Unknown age group' age group")
    