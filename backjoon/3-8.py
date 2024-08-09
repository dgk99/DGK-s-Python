import sys

n = int(input())
for num in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{num + 1}: {a} + {b} = {a + b}")