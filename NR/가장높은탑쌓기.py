n = int(input())

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(reverse=True)
dy = [0]*n
dy[0]=arr[0][1]
res=0
for i in range(1,n):
    MAX=0
    for j in range(0,i):
        if arr[i][2] < arr[j][2] and MAX < dy[j]:
            MAX= dy[j]

    dy[i] = MAX + arr[i][1]
    if res< dy[i]:
        res= dy[i]
print(res)