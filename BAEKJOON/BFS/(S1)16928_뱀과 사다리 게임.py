import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

g = [k for k in range(101)]
dist = [-1] * 101

for i in range(N + M) :
    x, y = map(int, input().split())
    g[x] = y

q = deque([1])
dist[1] = 0

while q :
    p = q.popleft()
    for i in range(1, 7) :
        n = p + i
        if n > 100:
            continue
        n = g[n]  
        if dist[n] == -1:
            dist[n] = dist[p] + 1
            q.append(n)

print(dist[100])

"""
g : 뱀, 사다리 리스트.
반복문에서 g[x] = y 설정해주면서 뱀, 사다리 설정.
만약 g[x] = y 처리 안해준 값들은 n = g[n] = n 이 된다.

dist : 방문 여부, 최소 숫자 체크
1~6 주사위에 대해
방문한 적이 없으면
이를 바꾸어주고 큐에 추가해준다. 
"""
