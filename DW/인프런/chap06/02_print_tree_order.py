# module
import sys

# input
sys.stdin = open("input.txt", "rt")

# 이진 트리 순회
## 이진 트리를 만들어 봤어요
tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [None, None],
        5: [None, None], 6: [None, None], 7: [None, None]}


## 전위 순회 출력
def preorder_print(node, storage):
    # None이 아닌 부모노드 저장
    if node is not None:
        storage.append(node)
    
    # 자식이 하나라도 있으면 돌아라
    if any(a is not None for a in tree[node]):
        # 왼쪽부터
        for i in tree[node]:
            preorder_print(i, storage)

    return storage


## 중위 순회 출력
def midorder_print(node, midliner):
    # 왼쪽 자녀가 있으면 왼쪽 자녀부터 계산
    if tree[node][0] is not None:
        midorder_print(tree[node][0], midliner)
    
    # 나 자신 들어가기
    midliner.append(node)
    
    # 오른쪽 자식 있으면 들어가기
    if tree[node][1] is not None:
        midorder_print(tree[node][1], midliner)

    return midliner


midorder_print(1, [])


## 후위 순회 출력
def postorder_print(node, storage):
    # 무조건 자녀부터 확인하는데 문제에서는 왼쪽부터 보기를 원함
    for i in tree[node]:
        if i is not None:
            postorder_print(i, storage)
    
    # 자녀 다 봤으면 자기 자신을 담는다.
    storage.append(node)

    return storage


print(*preorder_print(1, []))
print(*midorder_print(1, []))
print(*postorder_print(1, []))
