import sys
sys.stdin = open('input.txt','rt')

K, N = map(int, input().split())

lst = []

# MIN : 1cm
# MAX : 802cm (only one cut)
MIN = 1
MAX = 0
for _ in range(K) :
    x = int(input())
    lst.append(x)
    MAX = max(MAX, x)

result = 0

while MIN<=MAX :
    MID = (MIN+MAX)//2
    # cut
    cnt = 0
    for x in lst:
        cnt += x//MID
    # more cuts (MIN<MID<answer<MAX), okay
    if cnt>=N :
        result = MID
        MIN = MID+1
    # less cuts (MIN<anser<MID<MAX), not okay
    elif cnt < N :
        MAX = MID-1

print(result)