import sys
sys.stdin = open('input.txt','rt')

cards = list(range(1,21))

for _ in range(10) :
    start, end = map(int, input().split())
    cards[(start-1):end] = cards[(start-1):end][::-1]

print(cards)