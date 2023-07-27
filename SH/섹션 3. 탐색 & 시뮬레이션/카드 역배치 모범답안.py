import sys
sys.stdin = open('input.txt','rt')

cards = list(range(21))

for _ in range(10) :
    a, b = map(int, input().split())
    for i in range((b-a+1)//2) :
        # swap
        cards[a+i], cards[b-i] = cards[b-i], cards[a+i]

# remove 0
cards.pop(0)

for c in cards :
    print(c, end=' ')