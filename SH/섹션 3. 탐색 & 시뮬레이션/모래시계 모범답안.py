import sys
sys.stdin = open('input.txt','rt')

N = int(input())

A = [[0]*N for _ in range(N)]
for i in range(N) :
    row = list(map(int, input().split()))
    for j in range(N) :
        A[i][j] = row[j]

M = int(input())

# roatation

for i in range(M):
    row, to, rot = map(int, input().split())
    # left
    if to == 0:
        for _ in range(rot):
            A[row-1].append(A[row-1].pop(0))
    # right
    else:
        for _ in range(rot):
            A[row-1].insert(0, A[row - 1].pop())

# count

cnt = 0
s = 0
e = N-1

for i in range(N):
    for j in range(s, e+1):
        cnt += A[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(cnt)