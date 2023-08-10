import sys
sys.stdin = open('input.txt','rt')

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

MIN = 0
MAX = N-1

while MIN <= MAX :
    MID = (MIN+MAX)//2
    if lst[MID] == M :
        print(MID+1)
        break
    elif lst[MID] < M :
        MIN = MID+1
    else :
        MAX = MID-1