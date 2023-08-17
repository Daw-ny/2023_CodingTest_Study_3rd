# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 씨름 선수
n = int(input())
HoDong = []
for _ in range(n):
    HoDong.append(list(map(int, input().split())))
HoDong.sort(key=lambda x: (-x[1], -x[0]))

cnt = 0
HEIGHT = 0
for H, W in HoDong:
    if HEIGHT < H:
        HEIGHT = H
        cnt += 1

print(cnt)
