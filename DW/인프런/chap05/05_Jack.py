# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 공주 구하기
n, k = map(int, input().split())
Prince = [i for i in range(1, n+1)]
q = deque(Prince)
while len(q) > 1:
    cnt = 0
    while cnt < k - 1:
        q.append(q.popleft())
        cnt += 1
    q.popleft()
print(q[0])
