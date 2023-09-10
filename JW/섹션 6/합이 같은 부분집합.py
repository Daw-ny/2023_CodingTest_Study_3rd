import sys

def DFS(c,sum):
  if c==n:
    if sum==(MAX-sum):
      print('YES')
      sys.exit(0)
  else:
    DFS(c+1,sum+a[c])
    DFS(c+1,sum)

n=int(input())
a=list(map(int,input().split()))
MAX=sum(a)
DFS(0,0)
print('NO')
