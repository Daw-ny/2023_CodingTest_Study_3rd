# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 회문 문자열 검사
n = int(input())
for i in range(1, 1+n):
    s = input().lower()
    dab = 'YES'
    if len(s) % 2 == 0:
        for j in range(len(s)//2):
            if s[j] != s[-j-1]:
                dab = 'NO'
                break

    else:
        for j in range((len(s)-1)//2):
            if s[j] != s[-j-1]:
                dab = 'NO'
                break

    print('#'+str(i)+' '+dab)
