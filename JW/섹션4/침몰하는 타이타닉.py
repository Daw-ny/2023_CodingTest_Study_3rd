n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort(reverse=True)

c=1
kg=arr.pop(0)

while arr :

  if kg + arr[-1] <= m :
    kg += arr[-1]
    arr.pop()
  else:
    kg=arr.pop(0)
    c+=1

print(c)
