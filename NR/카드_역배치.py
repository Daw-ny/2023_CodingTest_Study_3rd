
cards = [i for i in range(1,21)]

for i in range(10):
    a,b = map(int, input().split())

    tmp1 = cards[:a-1]

    tmp2 = cards[a-1:b]

    tmp3 = cards[b:]

    cards = tmp1 + tmp2[::-1] + tmp3

print(*cards)

