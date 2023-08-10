import sys
sys.stdin = open('input.txt','rt')

N, M = map(int, input().split())

lst = list(map(int, input().split()))

MIN = max(lst)
MAX = sum(lst)

result = 0

while MIN<=MAX :
    MID = (MIN+MAX)//2
    # split
    cnt = 1
    one_disk = 0
    for x in lst :
        if one_disk + x > MID :
            cnt += 1
            one_disk = x
        else :
            one_disk += x
    # count(DVD) <= M (MIN<answer<MID<MAX), okay
    if cnt <= M :
        result = MID
        MAX = MID-1
    # count(DVD) > M (MIN<MID<answer<MAX), not okay
    elif cnt > M :
        MIN = MID+1

print(result)