n,m=map(int,input().split())
arr=[]

for i in range(n):
  arr.append(int(input()))


start=1
end=max(arr)

while start <= end :
  sum=0
  mid=(start+end)//2
  for i in arr :
    sum += i//mid
  if sum < m :
    end=mid-1
  else:
    start = mid +1

print(end)
