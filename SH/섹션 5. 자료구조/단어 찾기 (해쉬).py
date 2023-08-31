import sys

sys.stdin = open('input.txt','r')

N = int(input())

note = dict()
for _ in range(N):
    note[input()] = 0

for _ in range(N-1):
    note[input()] += 1

for k, v in note.items():
    if v == 0:
        print(k)