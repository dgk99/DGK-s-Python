x = int(input("x 좌표: "))
y = int(input("y 좌표: "))

if x >= 0 and y >= 0:
    print(1)
elif x < 0 and y >= 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)