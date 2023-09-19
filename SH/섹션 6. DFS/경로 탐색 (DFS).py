import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

res = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    res[start][end] = 1

check = [0]*(N+1)
cnt = 0

# start point is 1
path = [1]
check[1] = 1

def DFS(L):
    global cnt
    if L==N:
        cnt += 1
    else:
        for i in range(1, N+1):
            if res[L][i] == 1 and check[i] == 0:
                check[i] = 1
                path.append(i)
                DFS(i)
                check[i] = 0
                path.pop()
                
DFS(1)
print(cnt)