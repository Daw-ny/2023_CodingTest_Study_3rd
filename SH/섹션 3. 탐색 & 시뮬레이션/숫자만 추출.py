import sys
sys.stdin = open('input.txt', 'rt')

lst = list(input())

digit = ''
for l in lst :
    if l.isdigit() :
        digit += l
digit = int(digit)

print(digit)

cnt = 0
for i in range(1, digit+1) :
    if digit % i == 0 :
        cnt += 1

print(cnt)