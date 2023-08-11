# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 회의실 배정
n = int(input())
LOL = []
for _ in range(n):
    LOL.append(list(map(int, input().split())))
LOL.sort(key=lambda x: (x[1], x[0]))

TIME = 0
cnt = 0
q = deque(LOL)
while q:
    START, END = q.popleft()
    if TIME <= START:
        cnt += 1
        TIME = END
print(cnt)
