# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 주사위 게임
n = int(input())

first = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        tmp = a * 1000 + 10000
    elif a == b:
        tmp = a * 100 + 1000
    elif b == c:
        tmp = b * 100 + 1000
    elif a == c:
        tmp = a * 100 + 1000
    else:
        tmp = max([a, b, c]) * 100

    first = max(first, tmp)
print(first)
