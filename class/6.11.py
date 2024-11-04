# def 함수이름(매개변수):
#     함수 호출 시 실행 코드

# 함수 호출 시 입력 값을 전달할 수 있다.
# -> 1) Argument(인자 값)
# -> 2) Parameter(매개변수)

# def print_name(arg_name): # "arg_name" -> 매개변수
#     print(arg_name)
    
# print_name("개미") # "개미" -> 인자 값

# def get_sum(arg_a, arg_b, arg_c):
    
#     sum = arg_a + arg_b + arg_c
    
#     if sum < 0:
#         return # 함수 종료만 실행, 즉 반환 값 없음
    
#     avg = sum / 3
    
#     return sum, avg # -> (sum, avg)
#     # 함수 반환 값이 두 개 이상이면 -> 자동으로 tuple 자료형으로 구성 후 반환
    
# sum , avg = get_sum(1, 2, 3) # collection unpacking

# # call-by-value, call-by-reference


# # Primitive variables : sol, msg
# # Reference variables : bar, foo, kin

# sol = 4 # Number -> Primitive

# bar = [3, 4] # memory adress of list's head -> Reference

# foo = [5, 6] # "

# kin = bar # bar의 주소값을 그대로 가져온다 -> Reference

# kin[0] = 1 # kim[0]은 하나의 수식(Expression)이다.
# # [0]은 연산자로써, 이 코드가 실행되면 kin으로 가고, kin의 값을 읽어
# # 주소 값의 위치(리스트)로 이동하여 [0]의 값을 1로 바꾼다
# # 그래서 kin[0]은 Primitive가 아닌 Reference이다.   

# print(bar, foo, kin)
# # 메모리 상의 데이터를 가리키기 위한 포인터 역할을 하는 변수가 필요하다. 그 것이 참조변수이다.

# msg = "hello"

# kin.append(20)

# foo, kin = 7, 8


# bar = [3, 4, 5, 6]

# bar[1] = 10

# bar[2] = 20

# bar[0] = 90

# bar = [2, 3, 5]

# def foo(arg_list):
#     arg_list[1] = 100
    
# foo(bar)

# print(bar)


bar = [2, 3, 5]

def foo(arg_list):
    copied_list = arg_list[:]
    copied_list[0] = 100
foo(bar)
print(bar)

def kin(arg_list):
    arg_list[0] = 200
    
kin(bar.copy())

print(bar)