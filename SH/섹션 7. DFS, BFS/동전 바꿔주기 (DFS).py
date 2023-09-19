import sys

sys.stdin = open('input.txt','r')

T = int(input())
K = int(input())
lst = []
for _ in range(K):
    p, n = map(int, input().split())
    lst.append((p, n))

check = [0]*K
result = set()

def DFS(S):
    if S>T:
        return
    if S==T:
        # only tuple can be put
        result.add(tuple(check))
    else:
        for i in range(K):
            pi = lst[i][0]
            ni = lst[i][1]
            if check[i] < ni:
                check[i]+=1
                DFS(S+pi)
                check[i]-=1

DFS(0)

print(len(result))