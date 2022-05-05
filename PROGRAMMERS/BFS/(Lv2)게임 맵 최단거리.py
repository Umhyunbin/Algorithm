from collections import deque

def solution(maps):
    answer = 0
    visited = maps[:]
    
    N = len(maps)
    M = len(maps[0])
    q = deque([[0, 0]])
    while q: 
        p = q.popleft()
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 1):
                maps[nx][ny] = maps[p[0]][p[1]] + 1
                q.append([nx, ny])
        
    return maps[N - 1][M - 1] if maps[N - 1][M - 1] > 1 else -1
