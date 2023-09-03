n=int(input())
arr=[ input() for _ in range(n)]
arr2= [ input() for _ in range(n-1)]

arr.sort()
arr2.sort()

while True :
  x= arr.pop()
  y= arr2.pop()

  if x != y :
    print(x)
    break
  
  if len(arr)==1:
    print(arr[0])
    break
