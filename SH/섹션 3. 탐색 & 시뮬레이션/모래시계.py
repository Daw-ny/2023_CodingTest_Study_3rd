# 내 풀이 외에 모범답안도 공유되어 있음

import sys
sys.stdin = open('input.txt','rt')

N = int(input())

lst = [[0]*N for _ in range(N)]
for i in range(N) :
    row = list(map(int, input().split()))
    for j in range(N) :
        lst[i][j] = row[j]

# roatation : 규칙 찾아서 element 직접 이동시키기

M = int(input())

for _ in range(M) :
    num, direction, move = map(int, input().split())
    old = lst[num-1]
    new = [0]*N
    # left
    if direction == 0 :
        for i in range(N) :
            new[i-move] = old[i]
        lst[num-1] = new
    # right
    else :
        for i in range(N) :
            new[i+move-N] = old[i]
        lst[num-1] = new

# count : 카운트 방법이 1도 안 떠올라서 풀이 봄..

cnt = 0
start = 0
end = N-1

for i in range(N):
    for j in range(start, end+1):
        cnt += lst[i][j]
    if i < N//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1

print(cnt)