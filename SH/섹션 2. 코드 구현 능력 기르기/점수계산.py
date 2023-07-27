import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
lst = list(map(int, input().split()))

score = 0
successive = 0

for i in range(N) :
    if lst[i] == 1 :
        successive += 1
        score += successive
    else :
        successive = 0

print(score)