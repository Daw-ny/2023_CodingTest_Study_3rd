import sys
sys.stdin = open('input2.txt','r')

N = int(input())
R = list(map(int, input().split()))

A = [0]*N

# �������� ������ ó��
# n��° �ڷḦ ó���Ҷ� 1~(n-1)��° �ڷ�� �̹� �ڸ� ������Ƿ� �Ű澲�� �ʾƵ� ��
for i in range(N) :
    for j in range(N) :
        # R[i] : i+1��° �տ� ���� i+1��° ������ ū ���� R[i]��
        if R[i] == 0 and A[j] == 0 :
            A[j] = i+1
            break # �ڱ� �ڸ� ã�� �����ϱ� j �ݺ����� �ʿ� ����
        elif A[j] == 0 : # ���ڸ� �߰�
            R[i] -= 1

for a in A :
    print(a, end=' ')