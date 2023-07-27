# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 숫자만 추출
s = input()
n = ''
for c in s:
    if c.isnumeric():
        n += c


def cd(x):
    yak = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            yak.add(i)
            yak.add(x//i)
    return len(yak)


print(int(n))
print(cd(int(n)))
