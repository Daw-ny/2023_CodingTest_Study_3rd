import sys

sys.stdin = open('input.txt','r')

first = input()
second = input()

cnt = dict()
for i in range(len(first)):
    word = first[i]
    if word not in cnt.keys():
        cnt[word] = 1
    else:
        cnt[word] += 1

for i in range(len(second)):
    word = second[i]
    if word not in cnt.keys():
        break
    else:
        cnt[word] -= 1

for v in cnt.values():
    if v!=0:
        print('NO')
        break
else:
    print('YES')