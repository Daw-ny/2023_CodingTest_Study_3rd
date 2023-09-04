# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 합이 같은 부분집합
n = int(input())
lst = list(map(int, input().split()))
chk = [0] * (n + 1)


def dfs(points):
    if points == n+1: # 몇번 돌았는지 카운트 세기
        left = 0 # 좌변
        right = 0 # 우변
        for j in range(n):
            if chk[j] == 1: # 왼쪽으로 체킹
                left += lst[j]
            else: # 오른쪽으로 체킹
                right += lst[j]
        if left == right: # 왼 == 오른
            print("YES") # 같은 부분집합이 존재
            sys.exit(0) # 끄기

    else:
        # 역시나 백트래킹이 존재하는 구간
        chk[points] = 1
        dfs(points + 1)
        chk[points] = 0
        dfs(points + 1)


dfs(0)
print("NO") # 없으면 no를 출력해야함.
