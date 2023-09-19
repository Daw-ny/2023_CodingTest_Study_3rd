import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

res = [0]*M
cnt = 0

# L : level
# S : start number
def DFS(L, S):
    global cnt
    if L==M:
        # count + 1
        cnt += 1
        # print combination
        for j in range(M):
            print(res[j], end=' ')
        print()
    else:
        for i in range(S, N+1):
            res[L] = i
            DFS(L+1, i+1)

DFS(0, 1)
print(cnt)