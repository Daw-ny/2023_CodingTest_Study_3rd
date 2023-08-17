# module
import sys
import heapq

# input
#sys.stdin = open("input.txt", "rt")

# 창고 정리
L = int(input())
HEIGHT = list(map(int, input().split()))
M = int(input())

while M > 0:
    # 최댓값 뽑기
    MAX = heapq.nlargest(1, HEIGHT)[0]

    # 뽑은 다음 다시 heap으로 만들어줘야함
    HEIGHT = heapq.nlargest(len(HEIGHT), HEIGHT)[1:]
    heapq.heapify(HEIGHT)

    # 최소
    MIN = heapq.heappop(HEIGHT)

    # 1개 옮긴 것 표현
    heapq.heappush(HEIGHT, MIN + 1)
    heapq.heappush(HEIGHT, MAX - 1)

    # 1번 소모 O(M)시간 소모됨
    M -= 1
print(max(HEIGHT) - min(HEIGHT))
