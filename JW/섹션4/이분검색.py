n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()


start=0
end=len(arr)-1
c=0

while  start<=end:
  mid= (start+end) // 2
  if arr[mid]==m :
    print(mid+1)
    break
  elif arr[mid] > m :
    end = mid-1
  else:
    start=mid +1
