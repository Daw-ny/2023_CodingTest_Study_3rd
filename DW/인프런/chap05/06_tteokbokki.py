# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 응급실 떡볶이
n, m = map(int, input().split())
patient = list(map(int, input().split()))
cnt = 0
q = deque([i, j] for i, j in enumerate(patient))
stack = sorted(patient)

while q:
    a, b = q.popleft()
    if stack[-1] > b:
        q.append([a, b])
    elif a == m:
        break
    else:
        stack.pop()
        cnt += 1

print(cnt+1)
