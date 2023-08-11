# module
import sys
import heapq

# input
#sys.stdin = open("input.txt", "rt")

# 침몰하는 타이타닉
N, M = map(int, input().split())
WEIGHT = list(map(int, input().split()))
BOAT = 0
while WEIGHT:
    MAX = heapq.nlargest(1, WEIGHT)[0]
    WEIGHT = heapq.nlargest(len(WEIGHT), WEIGHT)[1:]
    heapq.heapify(WEIGHT)

    while WEIGHT and MAX + WEIGHT[0] <= M:
        MAX += heapq.heappop(WEIGHT)

    BOAT += 1

print(BOAT)
