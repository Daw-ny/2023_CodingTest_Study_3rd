import sys
from collections import deque

sys.stdin = open('input.txt','r')

N, M= map(int, input().split())

lst = list(map(int, input().split()))

dq = [(idx, danger) for idx, danger in enumerate(lst)]
dq = deque(dq)

cnt = 0

while dq:
    idx, danger = dq.popleft()
    if any(danger<d for _,d in dq):
        dq.append((idx, danger))
    else:
        cnt += 1
        if idx == M:
            break

print(cnt)