# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 알파코드
code = input()
n = len(str(code))
cnt = set()


def dfs(idx, word, lst):
    if word == '0': # 0은 강제 리턴
        return

    if word != '' and int(word) > 26: # 대문자 넘버링에 포함되지 않는 숫자면 리턴
        return

    if idx == n:
        lst.append(word) # 마지막 글자까지 포함
        global cnt
        if tuple(lst) not in cnt:
            print(''.join([chr(int(a) + 64) for a in lst])) # 바로 출력
        cnt.add(tuple(lst)) # 중복되는 단어가 존재할 수도 있기 때문에 여러번 출력하지 않게 조절
        lst.pop()
        return

    else:
        if word != '': # 아무것도 없을때 출력하면 안됨
            lst.append(word)
        dfs(idx + 1, code[idx], lst)
        if word != '':
            lst.pop()
        dfs(idx + 1, word + code[idx], lst)


dfs(0, '', [])
print(len(cnt))
