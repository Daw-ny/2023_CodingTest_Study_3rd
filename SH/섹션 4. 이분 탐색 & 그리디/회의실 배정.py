import sys
sys.stdin = open('input.txt','rt')

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

# It is important that the meeting be over quickly.
lst.sort(key=lambda x:(x[1], x[0]))

endtime = 0
cnt = 0

for start, end in lst :
    if start >= endtime :
        endtime = end
        cnt += 1

print(cnt)