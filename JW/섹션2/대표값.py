n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/n)
min = 9999999

for i in range(n):
    s=abs(a[i]-avg)
    if s < min :
        min =s
        a_s= a[i]
        num = i+1
    elif s== min :
        if a[i] > a_s:
            a_s= a[i]
            num = i+1

print(avg, num)
