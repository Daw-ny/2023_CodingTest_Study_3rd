# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# K번째 수
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))

    print("#%d %d" % (t+1, sorted(num[s-1:e])[k-1]))
