import sys
sys.stdin = open('input.txt', 'rt')

T = int(input())

for t in range(T) :
    _, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = lst[(s-1):e]
    lst.sort()
    print('#'+str(t+1)+' '+str(lst[k-1]))