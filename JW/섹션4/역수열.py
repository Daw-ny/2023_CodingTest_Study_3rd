import sys

input=sys.stdin.readline


n=int(input())
arr=list(map(int,input().split()))

result=[101]*len(arr) 

for i in range(n):
  c=0

  for j in range(n) :
    if arr[i]==0 and result[j]==101:
      result[j]=i+1
      break

    else:

      if result[j]> i+1:
        c+=1

      if c==arr[i] and result[j+1]==101:
        result[j+1]=i+1
        break

print(*result)
