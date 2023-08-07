# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 뮤직비디오
n, m = map(int, input().split())
number = list(map(int, input().split()))


def cnt(criteria):
    area = 1
    hap = 0
    q = deque(number)
    while q:
        a = q.popleft()
        if hap + a > criteria:
            hap = a
            area += 1
        else:
            hap += a
    return area


left = min(number)
right = sum(number)
while left <= right:
    middle = (left + right) // 2
    if cnt(middle) <= m:
        right = middle - 1
    else:
        left = middle + 1

print(left)
