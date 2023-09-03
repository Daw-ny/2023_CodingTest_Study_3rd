from collections import Counter
import sys
s1 = input()

s2 = input()

dic1 = Counter(s1)
dic2 = Counter(s2)

for k,v in dic1.items():
    if v != dic2.get(k,0):
        print("NO")
        sys.exit(0)

print('YES')
