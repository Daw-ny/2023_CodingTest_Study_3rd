# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 대표값
n = int(input())
num = list(map(int, input().split()))

lnum = list(map(lambda x: x - round(sum(num)/n), num))

tmp = [30000, -1]
for i, j in enumerate(lnum):
    if abs(tmp[0]) > abs(j):
        tmp = [j, i]
    elif abs(tmp[0]) == abs(j) and tmp[0] < j:
        tmp = [j, i]
print(round(sum(num)/n), tmp[1]+1)
