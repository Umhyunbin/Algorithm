import sys
from collections import deque

def bfs(g, loc):
    q = deque(loc)
    
    while q:
        coord = q.popleft()
        x, y = coord[0], coord[1]
        
        if x < N - 1 and g[x + 1][y] == 0:
            g[x + 1][y] = g[x][y] + 1
            q.append((x + 1, y))
        if x > 0 and g[x - 1][y] == 0:
            g[x - 1][y] = g[x][y] + 1
            q.append((x - 1, y))
        if y < M - 1 and g[x][y + 1] == 0:
            g[x][y + 1] = g[x][y] + 1
            q.append((x, y + 1))
        if y > 0 and g[x][y - 1] == 0:
            g[x][y - 1] = g[x][y] + 1
            q.append((x, y - 1))
    return g
        

M, N = map(int, sys.stdin.readline().rstrip().split())
li = []
location = []
for i in range(N):
    tmp = []
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for t in range(len(line)):        
        if line[t] == 1:
            location.append((i, t))
        tmp.append(line[t])
    li.append(tmp)

r = bfs(li, location)

if any(0 in a for a in r):
    print(-1)
else:
    print(max(map(max, r)) - 1)

"""
1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 빈 칸

다 1로 바꿀 수 있으면 그 최소날짜,
0이 1개라도 있으면 모든 토마토에 영향을 줄 수 없으므로 -1 출력.

bfs를 이용하여 자신의 값 + 1 을 인접한 값으로 설정.
"""
