import sys

input = sys.stdin.readline
st = input().rstrip()
bomb = input().rstrip()
b = len(bomb)
s = []

for i in st:
    s.append(i)
    if b <= len(s):
        if "".join(s[-b:]) == bomb:
            for _ in range(b):
                s.pop()

print("".join(s) if s else "FRULA")

"""
계속 replace하는건 문자열을 여러번 순회해야해서 시간복잡도에서 손해.
stack에 문자열을 추가하면서 bomb와 스택 마지막이 겹치면 pop하는 방식.
"""
