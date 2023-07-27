import sys
sys.stdin = open('input.txt','rt')

N, M = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0

for i in range(N+1) :
    for j in range(i+1, N+1) :
        if sum(seq[i:j]) == M :
            cnt += 1

print(cnt)