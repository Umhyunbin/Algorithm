import sys
from collections import deque

def bfs(g, b):    
    v = [[0] * N for _ in range(N)]
    v[b[0]][b[1]] = 1
    q = deque([(0, b)])
    
    result = []    
    while q:
        cnt, coord = q.popleft()
        cx, cy = coord        
        for i in range(4):            
            x = cx + nx[i]
            y = cy + ny[i]            
            if 0 <= x < N and 0 <= y < N and v[x][y] == 0:
                v[x][y] = 1
                if g[x][y] <= baby_size:
                    if 0 < g[x][y] < baby_size:
                        result.append([cnt + 1, (x, y)])                    
                    q.append((cnt + 1, (x, y)))                
    if result:
        result.sort()
        return result[0]
    else:
        return []

input = sys.stdin.readline
N = int(input())
sea = [list(map(int, input().rstrip().split())) for _ in range(N)]
nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

baby_loc = 0, 0
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            baby_loc = i, j
            
time, cnt = 0, 0
baby_size = 2
while True:               
    move = bfs(sea, baby_loc)    
    
    if not move:
        break
    else:
        runtime, n_loc = move
        x, y = n_loc
        past_x, past_y = baby_loc
        
        baby_loc = x, y
        sea[past_x][past_y] = 0                   
        sea[x][y] = 0
        
        time += runtime
        cnt += 1   
        
        if cnt == baby_size:    
            baby_size += 1
            cnt = 0
print(time)

"""
bfs로 먹을 수 있는 물고기를 다 먹고 (거리, 세로(x), 가로(y)) 기준으로 정렬하면
조건에 부합하는 최소를 반환할 수 있음.

0 < g[x][y] < baby_size -> 먹을 수 있는 물고기.
0 or baby_size -> 이동은 가능.

한 번 bfs를 할 때마다,
아기 상어 위치를 먹은 위치로 바꾸고,
이전 상어 자리 0으로 바꿔주고,
새로운 상어 위치도 0으로 바꾸고(물고기를 먹었으므로),
이동시간, 먹은 횟수를 추가시킨다.

이 때, 먹은 횟수는 각 size별로 count해야 함.
"""