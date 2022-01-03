def bfs(g):
    q = deque([(0, 0)])
        
    while q:
        x, y = q.popleft()
        if x + 1 < N and g[x+1][y] == 1:
            g[x+1][y] = g[x][y] + 1
            q.append((x+1, y))
        if x > 0 and g[x-1][y] == 1:
            g[x-1][y] = g[x][y] + 1
            q.append((x-1, y))
        if y + 1 < M and g[x][y + 1] == 1:
            g[x][y + 1] = g[x][y] + 1
            q.append((x, y + 1))
        if y > 0 and g[x][y - 1] == 1:
            g[x][y - 1] = g[x][y] + 1
            q.append((x, y - 1))
    return g

import sys
from collections import deque

# N : 세로, M : 가로
N, M = map(int,sys.stdin.readline().rstrip().split())
label = []
for i in range(N):
    line = sys.stdin.readline().rstrip()
    label.append([int(i) for i in line])   
        
r = bfs(label)
print(r[N - 1][M - 1])


"""
미로찾기 최단거리를 구해야 하는 문제.
인접한 값으로 이동할 때 1씩 더해주는 bfs 방식으로 문제 해결.


"""
