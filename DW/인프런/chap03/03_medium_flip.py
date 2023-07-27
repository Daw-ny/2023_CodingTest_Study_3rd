# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 카드 역배치
card = [i for i in range(1, 21)]
for _ in range(10):
    s, e = map(int, input().split())
    card = card[:s-1] + list(reversed(card[s-1:e])) + card[e:]
    
print(*card)
