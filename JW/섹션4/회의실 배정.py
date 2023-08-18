n=int(input())

arr=[]

for i in range(n):
  arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : (x[1],x[0]))

t=0
count=0

for j in arr:
  if t <= j[0]:
    t=j[1]
    count+=1

print(count) 
