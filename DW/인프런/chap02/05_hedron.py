# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 정다면체
n, m = map(int, input().split())

accident = [0] * (n + m + 1)
for i in range(1, n+1):
    for j in range(1, m+1):
        accident[i + j] += 1

maxnum = 0
candidate = []
for num, s in enumerate(accident):
    if s > maxnum:
        maxnum = s
        candidate = [num]
    elif s == maxnum:
        candidate.append(num)

print(*candidate)
