n=int(input())
arr=list(map(int,input().split()))
m=int(input())

r=[10001]*(m+1)
r[0]=0

for i in range(n):
  for j in range(arr[i],m+1):
    if r[j-arr[i]] != 10001:
      r[j]= min(r[j],r[j-arr[i]]+1)

print(r[m])
