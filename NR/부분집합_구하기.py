def dfs(L):
    if L==n+1:
        for i in range(len(visited)):
            if visited[i]==1:
                print(i, end=' ')
        print()
    else:

        visited[L]=1
        dfs(L+1)
        visited[L]=0
        dfs(L+1)

n = int(input())
visited=[0]*(n+1)
dfs(1)
