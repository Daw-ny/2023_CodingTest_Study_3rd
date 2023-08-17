import sys
sys.stdin = open('input.txt','rt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

cnt = 0

while lst :
    if len(lst) == 1 :
        cnt += 1
        break
    # two people
    if lst[0] + lst[-1] <= M :
        lst.pop(0)
        lst.pop()
        cnt += 1
    # one heavy person
    else :
        lst.pop()
        cnt += 1

print(cnt)