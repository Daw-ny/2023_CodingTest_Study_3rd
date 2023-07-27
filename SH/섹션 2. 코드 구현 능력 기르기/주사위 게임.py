import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

MAX = 0

for _ in range(N) :
    lst = list(map(int, input().split()))
    cnt = dict()
    for l in lst :
        if l not in cnt.keys() :
            cnt[l] = 1
        else :
            cnt[l] += 1
    # rule 1
    if len(cnt) == 1 :
        money = 10000 + lst[0]*1000
    # rule 3
    elif len(cnt) == 3 :
        money = max(lst) * 100
    # rule 2
    else :
        for k, v in cnt.items() :
            if v == 2 :
                money = 1000 + k * 1000
    # is MAX?
    if MAX < money :
        MAX = money

print(MAX)