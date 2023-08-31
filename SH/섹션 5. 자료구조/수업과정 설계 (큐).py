import sys
from collections import deque

sys.stdin = open('input.txt','r')

order = list(input())
N = int(input())

for i in range(N):
   plan = list(input())
   dq = deque(order)
   for p in plan:
       # must
       if p in dq:
           q = dq.popleft()
           # order X
           if p != q:
               print('#'+str(i+1)+' NO')
               break
   else:
        if len(dq)==0:
            print('#'+str(i+1)+' YES')
        else:
            print('#'+str(i+1)+' NO')