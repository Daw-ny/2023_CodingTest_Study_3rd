import sys

sys.stdin = open('input.txt','r')

N = int(input())
lst = list(map(int, input().split()))

check = [0]*N

def DFS(x):
    if x == N:
        SUM1 = 0
        SUM2 = 0
        for i in range(N):
            if check[i] == 1:
                SUM1 += lst[i]
            else:
                SUM2 += lst[i]
        if SUM1 == SUM2:
            print('YES')
            sys.exit()
    else:
        # set 1
        check[x] = 1
        DFS(x+1)
        # set 2
        check[x] = 0
        DFS(x+1)

DFS(0)

# if SUM1 != SUM2 for all nodes, print 'NO'
print('NO')