import sys
sys.stdin = open('input.txt','rt')

sudoku = [list(map(int, input().split())) for _ in range(9)]

for i in range(9) :
    row_check = [0]*9
    col_check = [0]*9
    for j in range(9) :
        # row check
        row_tmp = sudoku[i][j]-1
        if row_check[row_tmp] == 0 :
            row_check[row_tmp] = 1
        else :
            print('NO')
            sys.exit()
        # column check
        col_tmp = sudoku[i][j]-1
        if col_check[col_tmp] == 0 :
            col_check[col_tmp] = 1
        else :
            print('NO')
            sys.exit()

# box check
for i in range(0,9,3) :
    for j in range(0,9,3) :
        check = [0]*9
        # box
        for k in range(i, i+3) :
            for l in range(j, j+3) :
                tmp = sudoku[k][l]-1
                if check[tmp] == 0 :
                    check[tmp] = 1
                else :
                    print('NO')
                    sys.exit()
else :
    print('YES')