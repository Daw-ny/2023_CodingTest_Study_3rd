import sys
from collections import deque

sys.stdin = open('input.txt','r')

N, K = map(int, input().split())

deq = list(range(1,N+1))
deq = deque(deq)

while len(deq)>1 :
    for _ in range(K-1) :
        n = deq.popleft()
        deq.append(n)
    deq.popleft()

print(deq[0])