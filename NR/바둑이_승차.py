C, N = map(int, input().split())

dog = []

for i in range(N):
    dog.append(int(input()))

def dfs(L,SUM):
    global MAX
    if SUM>C:
        return
    if L==N:
        if MAX<SUM:
            MAX=SUM

    else:

        dfs(L+1,SUM+dog[L])
        dfs(L+1, SUM)
    return MAX
MAX=-9999999
print(dfs(0,0))
