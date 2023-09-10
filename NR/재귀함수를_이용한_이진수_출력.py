def DFS(n):
    if n>0:
        num = n//2
        res = n%2
        DFS(num)
        print(res , end='')
    else:
        return

n = int(input())
DFS(n)
