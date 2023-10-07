from collections import deque
s,e=map(int,input().split())


def bfs(s,e):
  answer=0
  v=[0]*100001 # ..?
  q=deque()
  q.append(s)
  v[s]=1
  c=0

  while(q):
      x=q.popleft()
    
      #앞으로 한칸, 뒤로 한칸, 5칸
      for i in (x-1,x+1,x+5):
        if i==e :
          return v[x]

        if 1 <= i <= 10001 and v[i]==0:
          v[i]=v[x]+1
          q.append(i)

print(bfs(s,e))
