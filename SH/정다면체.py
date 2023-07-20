import sys
sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())

SUM = dict()

for n in range(1, N+1) :
    for m in range(1, M+1) :
        s = n + m
        if s not in SUM.keys() :
            SUM[s] = 1
        else :
            SUM[s] += 1

MAX = 0
for v in SUM.values() :
    if MAX < v :
        MAX = v

for k in SUM.keys() :
    if SUM[k] == MAX :
        print(k, end=' ')