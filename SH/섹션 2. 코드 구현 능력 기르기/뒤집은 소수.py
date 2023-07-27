import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
lst = list(map(int, input().split()))

def reverse(x) :
    return int(str(x)[::-1])

def isPrime(x) :
    if x==1 :
        return False
    for i in range(2,x//2+1) :
        if x%i == 0 :
            return False
    else :
        return True

for l in lst :
    reverse_l = reverse(l)
    if isPrime(reverse_l) :
        print(reverse_l, end=' ')