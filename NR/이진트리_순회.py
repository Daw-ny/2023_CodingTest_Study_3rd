def DFS(n):

    if n>7:
        return
    else:
        # print(n, end=' ')
        DFS(n*2)
        # print(n, end=' ')
        DFS(n*2+1)
        print(n, end=' ')

DFS(1)
