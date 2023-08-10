import sys
sys.stdin = open('input.txt','rt')

N, C = map(int, input().split())

lst = [int(input()) for _ in range(N)]
lst.sort()

MIN = 1
MAX = lst[N-1]

result = 0

while MIN<=MAX :
    MID = (MIN+MAX)//2
    # put horse
    cnt = 1
    end = lst[0]
    for i in range(1,N) :
        if lst[i]-end >= MID :
            cnt += 1
            end = lst[i]
    # count(horse) >= M (MIN<MID<answer<MAX), okay
    if cnt >= C :
        result = MID
        MIN = MID+1
    # count(horse) < M (MIN<answer<MID<MAX), not okay
    else :
        MAX = MID-1

print(result)