from collections import deque

sub=input()
n=int(input())


for i in range(1,n+1):
  sub1=deque(sub)
  arr=deque(input())

  while arr:
    x=arr.popleft()

    if sub1:
      if x in sub1:
        if x==sub1[0]:
          sub1.popleft()
        else:
          print('#%d NO' %i)
          break
    if sub1==deque():
      print('#%d YES' %i)
      break

  else:
    print('#%d NO' %i)
