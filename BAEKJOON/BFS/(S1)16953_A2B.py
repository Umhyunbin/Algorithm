import sys
from collections import deque

input = sys.stdin.readline
A, B = map(int, input().rstrip().split())

q = deque([(A, 1)])
answer = -1

while q:
    num, cnt = q.popleft()
    
    if num * 2 == B or num * 10 + 1 == B:
        answer = cnt + 1
        break        
    
    if num * 2 < B:
        q.append((num * 2, cnt + 1))

    if num * 10 + 1 < B:
        q.append((num * 10 + 1, cnt + 1))    
print(answer)

"""
큐에 값, 연산횟수를 한 묶음으로 추가하기.
B보다 작을때만 추가하는 것으로 설정 -> 불필요한 탐색 X
"""
