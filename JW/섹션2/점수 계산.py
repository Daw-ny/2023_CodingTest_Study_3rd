n=int(input())
arr=input()
arr=arr.split('0')

count=0
for i in arr:
    c = i.count('1')
    
    for j in range(c):
        count += j+1

print(count)
