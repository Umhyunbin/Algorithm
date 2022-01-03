def calc(li):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                s = deque([[li[i][j], i, j]])                  
                while s:
                    p = s.popleft()
                    color = p[0]
                    x, y = p[1], p[2]
                    if visited[x][y] == 0:
                        visited[x][y] = 1
                        if y < N - 1 and li[x][y + 1] == color:
                            s.append([li[x][y + 1], x, y + 1])
                        if y > 0 and li[x][y - 1] == color:
                            s.append([li[x][y - 1], x, y - 1])
                        if x < N - 1 and li[x + 1][y] == color:
                            s.append([li[x + 1][y], x + 1, y])                            
                        if x > 0 and li[x - 1][y] == color:
                            s.append([li[x - 1][y], x - 1, y])
                cnt += 1
    return cnt


import sys
from collections import deque

N = int(input())
li_normal = [sys.stdin.readline().rstrip() for _ in range(N)]
li_abnormal = [i.replace("R", "G") for i in li_normal]
n = calc(li_normal)
a = calc(li_abnormal)
print(n, a)

"""
색깔 구역수를 구하는데
R, G, B에서 정상적인 사람, 적록색약인 사람 2가지를 구해야함.
정상을 기준으로 작성한 다음, R을 G로 바꾸어 다시 계산함.

0, 1로만 이루어져 있다면 1 -> 0으로 그래프 자체의 값을 바꿀 수 있는데
R, G, B 3가지로 이루어져 있기 때문에 visited 배열을 따로 만들어 계산함.

bfs의 while문에서 4가지 방향에 대해 방문여부를 묻고 추가한다면
append 연산횟수가 줄어들 것으로 기대됨.
(물론 append 하더라도 이미 방문했던 곳이라면 큰 if문에서 걸러짐.)

"""
