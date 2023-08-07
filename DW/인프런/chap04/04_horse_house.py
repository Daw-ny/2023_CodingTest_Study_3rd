# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 마구간 정하기
n, c = map(int, input().split())
point = []
for _ in range(n):
    point.append(int(input()))

point.sort()


def cnt(criteria):
    area = 1
    s = point[0]
    for i in range(1, n):
        if point[i] - s >= criteria:
            s = point[i]
            area += 1
    return area


left = 0
right = point[-1] - point[0]
while left <= right:
    middle = (left + right) // 2
    if cnt(middle) < c:
        right = middle - 1
    else:
        left = middle + 1
print(right)
