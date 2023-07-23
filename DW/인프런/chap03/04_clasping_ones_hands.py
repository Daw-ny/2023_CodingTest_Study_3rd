# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 두 리스트 합치기
numlist = []
for _ in range(2):
    n = int(input())
    numlist += list(map(int, input().split()))

print(*sorted(numlist))
