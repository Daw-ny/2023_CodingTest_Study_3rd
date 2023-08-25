# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 가장 큰 수
n, m = input().split()
k = int(m)
q = deque(n)
stack = deque()

while q:
    a = q.popleft()
    while stack and a > stack[-1] and k > 0:
        stack.pop()
        k -= 1
    stack.append(a)

print(''.join(list(stack))[:(len(n)-int(m))])
