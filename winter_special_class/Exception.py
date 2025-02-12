# 1. 사용자 입력 오류
# num = int(input(" 1 또는 2를 입력하세요: "))

# try:
#     if num == 1:
#         raise ValueError
#     else:
#         raise NameError

# except ValueError:
#     print("ValueError 예외 발생")
    
# except NameError:
#     print("NameError 예외 발생")

# try:
#     print("pos")
#     print(1/0) # 주석 처리 on/off에 따른 결과 값 확인
#     print("bar")
#     kin() # 주석 처리 on/off에 따른 결과 값 확인
    
#     raise IndexError("인덱스 예외 발생생")
# except ValueError:
#     print("ValueError 예외 발생")
# except IndexError as e:
#     print(f"예외 발생: {e}")
# except NameError as e:
#     print(f"예외 발생: {e}")
# except ZeroDivisionError:
#     print("ZeroDivisionError 예외 발생")
    
    
# try:
#     print(1)
    
#     print(2)
    
#     result = 1 / 0
    
#     print(4)
    
# except ZeroDivisionError:
#     print(5)

# print(6)

# try:
#     print(1)
    
#     result = 1 / 0
    
#     print(2)
    
#     print(3)
# except Exception:
#     print(3.5)
# except ZeroDivisionError:
#     print(4)
# except NameError:
#     print(5)
# except OSError:
#     print(6)
# print(7)

num = 1

try:
    print(1)
    
    if num == 1:
        raise KeyboardInterrupt

    print(2)
    
except KeyboardInterrupt:
    print(4)
    
else:
    print(5)
finally:
    print(6)

print(7)