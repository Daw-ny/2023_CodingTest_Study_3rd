n=int(input())
arr=list(map(int,input().split()))

v=[1]*n
count=0

for i in range(1,n):
  for j in range(i-1,-1,-1):
    if arr[j] < arr[i] :
      v[i]=max(v[i],v[j]+1)
  count=max(count,v[i])

print(count)
