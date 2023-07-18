def digit_sum(x):
    sum=0

    for j in range(len(x)):
        sum+= int(x[j])
    
    return sum

n=int(input())
arr=list(input().split())
t=0
s=0

for i in arr:
    if s < digit_sum(str(i)):
        s=digit_sum(str(i))
        t=i

print(t)
