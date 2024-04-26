# import random

# # 리스트 생성 : bar(참조변수)
# bar = list()

# for _ in range(0, 5): # 0, 1, 2, 3, 4
#     # random.randint(1, 100) -> 1이상 100이하의 정수 중 난수를 한 개 선택
#     bar.append(random.randint(1, 100))
# print(bar)


# print(bar[4], bar[-1], bar[len(bar) - 1])

# bar = [10, 20, 30, 40, 50]

# print( bar[0] )
# print( bar[1] )
# print( bar[2] )
# print( bar[3] )
# print( bar[4] )
# # print( bar[5] )

# print( bar[-1] )
# print( bar[-2] )
# print( bar[-3] )
# print( bar[-4] )
# print( bar[-5] )
# # print( bar[-6] )

# bar = [ 10, 20, 30, 40 ]

# foo = bar[0:0:1]
# print(foo)
# foo = bar[0:1:1]
# print(foo)
# foo = bar[0:2:1]
# print(foo)
# foo = bar[0:3:1]
# print(foo)
# foo = bar[0:4:1]
# print(foo)
# foo = bar[1:4:1]
# print(foo)

# bar = [ 10, 20, 30, 40 ]

# # 빈칸일 경우, index0과 index-1까지 +1씩
# foo = bar [ : ]
# print(foo)
# # stop값이 없을 경우, index2부터 index-1까지 +1씩
# foo = bar [ 2 : ]
# print(foo)
# # start값이 없을 경우, index0부터 index3 까지 +1씩
# foo = bar [ : 3 ]
# print(foo)

# # 이 값이 [ ] 공백인 이유 : 
# # step값이 +1이라서 -1 = 40 이후로 숫자가 없기에 공백
# foo = bar[-1 : -4]
# print(foo) 
# # stop값이 생략되고, 시작값이 -1, step값이 -1이면 위 처럼 역순으로 출력된다.
# foo = bar[-1 ::-1]
# print(foo)

# 770225-3983813
# 3개로 구분해서 문자열로 저장
bar = [7,7,0,2,2,5,'-',3,9,8,3,8,1,3]
# 1. 생년월일 6자리 -> 770225
foo = bar[0 : 6]
print(foo)
# 2. 지역 코드값 6자리 -> 398381
foo = bar[7 : 13]
print(foo)
# 3. 패리티 체크값 1자리 -> 3
pos = bar[-1]
print(pos)

print(type(pos))
