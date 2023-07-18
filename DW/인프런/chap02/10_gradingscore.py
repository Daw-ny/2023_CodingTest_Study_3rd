# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 점수 계산
n = int(input())
score = list(map(int, input().split()))
hap = 0
bonus = 0
for s in score:
    if s:
        bonus += 1
        hap += bonus
    else:
        bonus = 0
print(hap)
