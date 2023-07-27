import sys
sys.stdin = open('input.txt','rt')

N = int(input())

lst = [[0]*N for _ in range(N)]
for i in range(N) :
    row = list(map(int, input().split()))
    for j in range(N) :
        lst[i][j] = row[j]

MAX = 0

# diagonal sum
diag_sum_1 = 0
diag_sum_2 = 0

for i in range(N) :
    row_sum = 0
    col_sum = 0
    for j in range(N) :
        # row sum
        row_sum += lst[i][j]
        # column sum
        col_sum += lst[j][i]
    if MAX < row_sum :
        MAX = row_sum
    if MAX < col_sum :
        MAX = col_sum
    # diagonal sum
    diag_sum_1 += lst[i][i]
    diag_sum_2 += lst[i][N-(i+1)]

if MAX < diag_sum_1 :
    MAX = diag_sum_1
if MAX < diag_sum_2 :
    MAX = diag_sum_2

print(MAX)