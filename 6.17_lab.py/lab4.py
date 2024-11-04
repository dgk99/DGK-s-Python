# max_of_three(a,b,c) 함수 작성

def max_of_three(arg_a, arg_b, arg_c):
    if arg_a > arg_b and arg_a > arg_c:
        return arg_a
    elif arg_b > arg_a and arg_b > arg_c:
        return arg_b
    else:
        return arg_c

print(max_of_three(10, 20, 15)) # 20