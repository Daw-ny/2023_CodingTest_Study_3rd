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
        # ��տ� ���� ����� ��
        min_s = l
        # �ش� ���� ��ȣ
        min_i = idx+1
    elif diff == MIN :
        if l > min_s :
            min_s = l
            min_i = idx+1

print(min_i)