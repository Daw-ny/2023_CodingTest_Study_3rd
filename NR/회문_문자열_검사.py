n = int(input())


for i in range(n):
    s = input().lower()
    if s == s[::-1]:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')