# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 중복 순열
n, m = map(int, input().split())
cnt = 0
lst = [0]*n


# 중복순열 함수
def hyperlimitpermutation(num):
    global lst, cnt
    if num == m: # 원하는 구간까지 다 채웠으면 m번째 자리부터는 drop
        print(*lst[:m])
        cnt += 1

    else:
        for i in range(1, n+1): # 앞에서부터 1 ~ n까지 채우는 단계 
            lst[num] = i
            hyperlimitpermutation(num + 1)


hyperlimitpermutation(0)
print(cnt)
