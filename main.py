N = int(input())
M = map(int, (input().split()))
x = int(input())

print(min(M, key=lambda a : abs(a - x)))
