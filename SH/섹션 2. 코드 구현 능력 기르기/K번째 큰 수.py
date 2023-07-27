import sys
sys.stdin = open('input.txt', 'rt')

N, K = map(int, input().split())

lst = list(map(int, input().split()))

sums = set()
for i in range(N) :
    for j in range(i+1, N) :
        for l in range(j+1, N) :
            # set : add (no append)
            sums.add(lst[i]+lst[j]+lst[l])

sums = list(sums)
sums.sort(reverse=True)
print(sums[K-1])