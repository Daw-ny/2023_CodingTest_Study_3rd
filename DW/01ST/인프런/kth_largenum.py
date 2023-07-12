# module
import sys
from itertools import combinations

# input
#sys.stdin = open("input.txt", "rt")

# K번째 큰 수
n, k = map(int, input().split())
num = list(map(int, input().split()))

# 저장 하기
s = set()
for c in list(combinations(num, 3)):
    s.add(sum(c))
print(sorted(s, reverse=True)[k-1])
