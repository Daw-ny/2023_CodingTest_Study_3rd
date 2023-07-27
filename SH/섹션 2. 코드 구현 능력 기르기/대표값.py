import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
lst = list(map(int, input().split()))

# average score
avg = round(sum(lst)/N)
print(avg, end=' ')

# nearest student
MIN = float('inf')

for idx, l in enumerate(lst) :
    diff = abs(l-avg)
    if diff < MIN :
        MIN = diff
        # 평균에 가장 가까운 값
        min_s = l
        # 해당 값의 번호
        min_i = idx+1
    elif diff == MIN :
        if l > min_s :
            min_s = l
            min_i = idx+1

print(min_i)