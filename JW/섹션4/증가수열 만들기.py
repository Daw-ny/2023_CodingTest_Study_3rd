n=int(input())
arr=list(map(int,input().split()))

r=''
c=0
while True :
  if arr[0]>=c and arr[-1] >=c :
    if min(arr[0],arr[-1])==arr[0]:
      r+='L'
      c=arr[0]
      arr.pop(0)
    else:
      r+='R'
      c=arr[-1]
      arr.pop()
  elif arr[0] >=c and arr[-1] < c:
    r+='L'
    c=arr[0]
    arr.pop(0)
  elif arr[0] < c and arr[-1] >= c:
    r+='R'
    c=arr[-1]
    arr.pop()
  else:
    break

print(len(r))
print(r)
