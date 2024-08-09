n = int(input())
for i in range(n):
    for b in range(n - 1):
        print(" ", end="")
    for s in range(i + 1):
        print("*", end="")
    print()
    n -= 1