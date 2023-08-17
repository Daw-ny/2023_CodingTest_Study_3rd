import sys
sys.stdin = open('input.txt','rt')

N = int(input())
lst = list(map(int, input().split()))

MIN = 0
result = ''

while True :
    # condition 1 : finish
    if lst[0] < MIN and lst[-1] < MIN :
        break
    # condition 2 : left or right
    elif lst[0] > MIN and lst[-1] > MIN :
        # left
        if lst[0] < lst[-1] :
            MIN = lst[0]
            lst.pop(0)
            result += 'L'
        # right
        else :
            MIN = lst[-1]
            lst.pop()
            result += 'R'
    # condition 3 : left
    elif lst[0] > MIN and lst[-1] < MIN :
        MIN = lst[0]
        lst.pop(0)
        result += 'L'
    # condition 4 : right
    elif lst[0] < MIN and lst[-1] > MIN :
        MIN = lst[-1]
        lst.pop()
        result += 'R'

print(len(result))
print(result)