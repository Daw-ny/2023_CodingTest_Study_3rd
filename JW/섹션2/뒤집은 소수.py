def reverse(x):
    n=str(x)
    return int(n[::-1])

def isPrime(x):
    for i in range(2,int(x**1/2)+1):
        if x % i ==0 :
            return False
    return True

n=int(input())
arr=list(map(int,input().split()))

r=[]
for i in arr :
    x=reverse(i)
    if x>=2 and isPrime(x)==True :
        r.append(x)
print(*r)
