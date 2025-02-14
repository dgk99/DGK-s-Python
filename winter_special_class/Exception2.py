num = 1

try:
    print(10)
    
    if num == 1:
        raise ValueError
    else:
        raise ZeroDivisionError
    
    print(20)
except Exception:
    print(22)
except ZeroDivisionError:
    print(30)
print(40)
