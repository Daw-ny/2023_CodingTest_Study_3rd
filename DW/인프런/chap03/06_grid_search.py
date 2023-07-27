# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 격자판 최대합
n = int(input())
mabangjin = []
for _ in range(n):
    mabangjin.append(list(map(int, input().split())))

hap = []
for j, k in zip(mabangjin, zip(*mabangjin)):
    hap.append(sum(j))
    hap.append(sum(k))

left = 0
right = 0
for i in range(n):
    left += mabangjin[i][i]
    right += mabangjin[i][n-1-i]
hap.append(left)
hap.append(right)

print(max(hap))
