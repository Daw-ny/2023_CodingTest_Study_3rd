import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
lst = list(map(int, input().split()))

def digit_sum(x) :
    SUM = 0
    while x>0 :
        SUM += x%10 # remainder
        x = x//10 # quotient
    return SUM

MAX = 0

for l in lst :
    ds = digit_sum(l)
    if MAX < ds :
        MAX = ds
        MAX_int = l

print(MAX_int)
