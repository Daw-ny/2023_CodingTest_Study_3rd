# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 역수열
N = int(input())
CNT = list(map(int, input().split()))

LIST = [0]*N
for i, j in enumerate(CNT, start=1):
    MOVE = j
    while LIST[:MOVE].count(0) < j or LIST[MOVE] != 0:
        MOVE += 1
    LIST[MOVE] = i
print(*LIST)
