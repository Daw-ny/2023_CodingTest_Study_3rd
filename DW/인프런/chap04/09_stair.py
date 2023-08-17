# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 증가수열 만들기
N = int(input())
ARRAY = deque(list(map(int, input().split())))

q = deque([[0, N-1, '', 0, deque([0])]])
LEFT = 0
RIGHT = N-1


while q:
    LEFT, RIGHT, TEXT, CNT, stack = q.popleft()

    if ARRAY[LEFT] > stack[-1] and LEFT < RIGHT:
        stack.append(ARRAY[LEFT])
        q.append([LEFT + 1, RIGHT, TEXT + 'L', CNT + 1, stack.copy()])
        stack.pop()

    if ARRAY[RIGHT] > stack[-1] and LEFT < RIGHT:
        stack.append(ARRAY[RIGHT])
        q.append([LEFT, RIGHT - 1, TEXT + 'R', CNT + 1, stack.copy()])
        stack.pop()

print(len(stack) - 1)
print(TEXT)
