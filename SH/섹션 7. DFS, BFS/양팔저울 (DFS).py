import sys

sys.stdin = open('input.txt','r')

N = int(input())
lst = list(map(int, input().split()))

weights = [0]*(sum(lst)+1)
check = [0]*N

def DFS(L):
    if L==N:
        left = 0
        right = 0
        for i in range(N):
            if check[i] == 1:
                left += lst[i]
            elif check[i] == 2:
                right += lst[i]
        weight = abs(left-right)
        weights[weight] = 1
    else:
        # left
        check[L] = 1
        DFS(L+1)
        # right
        check[L] = 2
        DFS(L+1)
        # none
        check[L] = 0
        DFS(L+1)

DFS(0)

cnt = 0
for w in weights:
    if w == 0:
        cnt += 1
print(cnt)