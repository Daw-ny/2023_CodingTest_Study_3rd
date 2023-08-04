# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 이분검색
n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))

left = 0
right = n
middle = 0
while number[middle] != m:
    middle = (left + right)//2
    if number[middle] > m:
        right -= 1
    elif number[middle] < m:
        left += 1
print(middle + 1)
