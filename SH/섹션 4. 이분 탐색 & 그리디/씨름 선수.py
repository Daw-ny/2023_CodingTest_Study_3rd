import sys
sys.stdin = open('input.txt','rt')

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

# sort key : height
lst.sort(reverse=True)

# only check weight!
max_weight = lst[0][1]
cnt = 0

for _, weight in lst :
    if weight >= max_weight :
        max_weight = weight
        cnt += 1

print(cnt)