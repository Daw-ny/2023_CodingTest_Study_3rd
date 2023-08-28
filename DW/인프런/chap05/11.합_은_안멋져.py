# module
import sys
import heapq

# input
#sys.stdin = open("input.txt", "rt")

# 최소 힙
Hop = []
while True:
    n = int(input())
    if n == -1:
        break

    elif n == 0 and Hop:
        print(-heapq.heappop(Hop))

    elif n not in [-1, 0]:
        heapq.heappush(Hop, -n)
