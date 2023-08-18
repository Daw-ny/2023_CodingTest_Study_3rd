n=int(input())

arr=[]

for _ in range(n):
  arr.append(list(map(int,input().split())))

arr.sort(key=lambda x: x[0])

c=1
for i in range(n-1):
  weight=arr[i][1]
  for j in range(i+1,n):
    if weight <= arr[j][1]:
      break
  else:
        c+=1

print(c)
