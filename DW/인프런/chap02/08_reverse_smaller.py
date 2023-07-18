# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 뒤집은 소수
n = int(input())
numlist = list(input().split())


# 두 함수
def reverse(x):
    rx = ''
    for c in range(len(x)-1, -1, -1):
        rx += x[c]
    return int(rx)


def isPrime(x):
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            return False
    return True if x != 1 else False


rlist = list(map(reverse, numlist))
dab = []
for s in rlist:
    if isPrime(s):
        dab.append(s)

print(*dab)
