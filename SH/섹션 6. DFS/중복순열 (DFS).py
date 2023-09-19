import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

res = [0]*M
cnt = 0

def DFS(L):
    global cnt
    if L==M:
        # count
        cnt += 1
        # print permutation w/ repetition
        for r in res:
            print(r, end=' ')
        print()
    else:
        # Lth element of the permutation
        for i in range(1, N+1):
            res[L] = i
            DFS(L+1)

DFS(0)
print(cnt)