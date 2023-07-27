# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 수 들의 합
n, m = map(int, input().split())
numlist = list(map(int, input().split()))
q = deque(numlist)
q2 = deque()
num = 0
cnt = 0

while q:
    if num < m:
        q2.append(q.popleft())
        num += q2[-1]

    elif num == m:
        cnt += 1
        num -= q2.popleft()

    else:
        num -= q2.popleft()

while num >= m:
    if num == m:
        cnt += 1
    num -= q2.popleft()

print(cnt)
