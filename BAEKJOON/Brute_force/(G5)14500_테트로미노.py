import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 모든 유형의 테트로미노를 탐색하도록 함
def dfs(r, c, idx, total): # idx는 칸의 수, total은 칸에 쓰인 수들의 합
    global ans
    # 가지치기. 테트로미노 모양에 맞게 탐색한 최대 결과보다 ans가 크면 그냥 return.
    if ans >= total + max_val * (3 - idx):
        return
    # 4개의 정사각형을 탐색했으면 리턴
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                # 2번째에서 ㅜ와 ㅁ을 만들 수 있어서 -> 새로운 값 기준이 아닌 기존 값 기준.
                if idx == 1:
                    visited[nr][nc] = 1
                    dfs(r, c, idx+1, total + arr[nr][nc])
                    visited[nr][nc] = 0
                visited[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visited[nr][nc] = 0


N, M = map(int, input().split()) # N: 세로크기, M: 가로크기
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

ans = 0
max_val = max(map(max, arr))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1  # 이번 반복문의 기준값이므로 이미 방문 처리.
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0  # 다음 반복문에서는 (i, j)가 다시 탐색 대상이다.

print(ans)

"""
dfs를 이용하여 테트로미노 모양으로 탐색 진행.
"""