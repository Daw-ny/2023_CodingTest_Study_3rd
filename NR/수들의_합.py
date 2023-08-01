m, n = map(int, input().split())

array = list(map(int, input().split()))

SUM = 0
cnt =0

i=0
j=1
while j<=m:

    SUM = sum(array[i:j])

    if SUM < n:
        j+=1
    elif SUM==n:
        cnt+=1
        SUM-=array[i]
        i+=1
    elif SUM > n:
        SUM-=array[i]
        i+=1
print(cnt)
