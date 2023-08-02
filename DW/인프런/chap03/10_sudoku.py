# module
import sys
from collections import Counter

# input
#sys.stdin = open("input.txt", "rt")

# 스도쿠 검사
sudoku = []
for _ in range(9):
    lst = list(map(int, input().split()))
    sudoku.append(lst)

for r, c in zip(sudoku, zip(*sudoku)):
    one = list(Counter(r).values()).count(1)
    two = list(Counter(c).values()).count(1)
    if one != 9 or two != 9:
        print('NO')
        break
else:
    dic = Counter()
    for i in range(6):
        for j in range(6):
            dic[sudoku[i][j]] += 1
    if list(dic.values()).count(4) != 9:
        print('NO')
    else:
        print('YES')


