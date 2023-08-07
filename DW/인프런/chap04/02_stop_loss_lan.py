# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 랜선 자르기
n, k = map(int, input().split())
number = []
for _ in range(n):
    number.append(int(input()))

left = 0
right = max(number)
while left <= right:
    middle = (left + right)//2
    cnt = sum(list(map(lambda x: x//middle, number)))
    if cnt >= k:
        left = middle + 1
    elif cnt < k:
        right = middle - 1

print(right)
