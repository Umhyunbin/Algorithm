import sys
from collections import deque

def bfs(g, loc):
    q = deque(loc)
    
    while q:
        coord = q.popleft()
        x, y, h = coord[0], coord[1], coord[2]
        
        if x < N - 1 and g[h][x + 1][y] == 0:
            g[h][x + 1][y] = g[h][x][y] + 1
            q.append((x + 1, y, h))
        if x > 0 and g[h][x - 1][y] == 0:
            g[h][x - 1][y] = g[h][x][y] + 1
            q.append((x - 1, y, h))
        if y < M - 1 and g[h][x][y + 1] == 0:
            g[h][x][y + 1] = g[h][x][y] + 1
            q.append((x, y + 1, h))
        if y > 0 and g[h][x][y - 1] == 0:
            g[h][x][y - 1] = g[h][x][y] + 1
            q.append((x, y - 1, h))
        if h < H - 1 and g[h + 1][x][y] == 0:
            g[h + 1][x][y] = g[h][x][y] + 1
            q.append((x, y, h + 1))
        if h > 0 and g[h - 1][x][y] == 0:
            g[h - 1][x][y] = g[h][x][y] + 1
            q.append((x, y, h - 1))
    return g
        

M, N, H = map(int, sys.stdin.readline().rstrip().split())
li = []
location = []
for h in range(H):
    htmp = []
    for i in range(N):
        tmp = []
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        for t in range(len(line)):        
            if line[t] == 1:
                location.append((i, t, h))
            tmp.append(line[t])
        htmp.append(tmp)
    li.append(htmp)

r = bfs(li, location)

v = 0
flag = True
for i in range(H):
    for j in range(N):
        for k in range(M):
            if r[i][j][k] == 0:
                print(-1)
                flag = False
                break
        if not flag:
            break
        v = max(v, max(r[i][j]))
    if not flag:
        break
if flag:      
    print(v - 1)

"""
토마토 2D 와 같은 스타일의 문제.
3차원으로 생각해야 해서
갈 수 있는 방향을 4개가 아닌, 6개로 설정.
"""
