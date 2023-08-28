# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 단어 찾기
n = int(input())
dic = {}
for _ in range(n):
    dic[input()] = 1

for _ in range(n-1):
    del dic[input()]

print(*list(dic.keys()))
