# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 부분집합 구하기
n = int(input())
lst = [0] * (n + 1)


# 부분집합 만들기
def dfs(num):
    if num == n+1: # 여기는 카운트를 세는 곳. n = 5이면 n = 6일 때 멈춰서 재귀 정지를 진행함
        for i in range(1, n+1): # 1부터 세야함
            if lst[i] == 1: # 1이면 출력 계속 해주기
                print(i, end=' ')
        print()

    else:
        lst[num] = 1
        dfs(num + 1) # 채우고 다음으로 넘어가기
        lst[num] = 0
        dfs(num + 1) # 백트래킹 역할을 해주는 것


dfs(1)
