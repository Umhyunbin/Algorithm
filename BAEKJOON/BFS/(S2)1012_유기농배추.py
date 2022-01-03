def calc(li, M, N):
    cnt = 0
    for i in range(N):
        for j in range(M):                  
            if li[i][j] == 0:
                continue
            else:                
                q = deque([[i, j]])           
                while q:
                    p = q.popleft()
                    x, y = p[0], p[1]  
                    
                    if y < M - 1 and li[x][y + 1] == 1:
                        li[x][y + 1] = 0
                        q.append([x, y + 1])                      
                    if y > 0 and li[x][y - 1] == 1:
                        li[x][y - 1] = 0
                        q.append([x, y - 1])                       
                    if x < N - 1 and li[x + 1][y] == 1:
                        li[x + 1][y] = 0
                        q.append([x + 1, y])                        
                    if x > 0 and li[x - 1][y] == 1:
                        li[x - 1][y] = 0
                        q.append([x - 1, y])  
                cnt += 1               
    return cnt


import sys
from collections import deque

T = int(input())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    v = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        v[Y][X] = 1
    print(calc(v, M, N))

"""
몇 개의 그룹으로 나누어져 있는지 찾는 문제와 같은 문제이다.
배추가 있으면서 아직 방문하지 않는 start point를 반복문을 통해 시작.

이 point를 기준으로 bfs 진행.
4가지 방향에 대하여 조사하여 만약 그 방향에 대한 값이 1이면
0으로 만들고(추후 탐색 불가능하게 만듬) 그 값의 4가지 방향을 조사하기 위해
q에 추가한다.
"""
