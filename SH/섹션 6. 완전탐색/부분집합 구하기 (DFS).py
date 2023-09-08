import sys

sys.stdin = open('input.txt','r')

N = int(input())

check = [0]*(N+1)

def DFS(x):
    # check completed! (from 1 to N)
    if x == N+1:
        for i in range(1, N+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
    else:
        # check O
        check[x] = 1
        DFS(x+1)
        # check X
        check[x] = 0
        DFS(x+1)

DFS(1)