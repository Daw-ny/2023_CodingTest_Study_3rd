# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 자릿수의 합
n = int(input())
nature = list(input().split())


# digit_sum
def digit_sum(x):
    hap = 0
    for s in x:
        hap += int(s)
    return hap


# compare num
first = -1
sumn = 0
for c in range(n):
    tmp = digit_sum(nature[c])
    if tmp > sumn:
        sumn = tmp
        first = c

print(nature[first])
