import sys

K = int(sys.stdin.readline().rstrip())
S = []

for i in range(K):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        S.append(num)
    else:
        S.pop()
print(sum(S))

"""
num이 0 아닌 경우  -> S에 append
num이 0 인 경우 -> S에서 pop
"""
