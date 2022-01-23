import sys
from math import inf

def floyd(g, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g[i][j] > g[i][k] + g[k][j]:
                    g[i][j] = g[i][k] + g[k][j]
    return g

N, M = map(int, sys.stdin.readline().rstrip().split())

c = [[inf] * N for _ in range(N)]

for i in range(N):
    c[i][i] = 0
    
for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    c[x-1][y-1] = 1
    c[y-1][x-1] = 1

r = floyd(c, N)

answer = inf, inf
for i in range(N):
    s = sum(r[i])
    if s < answer[1]:
        answer = i + 1, s
    
print(answer[0])

"""
모든 정점 사이의 최단 경로를 찾는 탐색 알고리즘은 Floyd-Warshall 이용.
O(N^3) 이라 N의 크기가 중요한데 N <= 100이라서 사용해도 괜찮다고 판단함.

간선 가중치가 부여되지 않은 상황이므로 이런 알고리즘 말고 bfs 이용해도 괜찮다.
bfs를 이용한다면
n = [0] * (N + 1)
q = deque([start])
v[start] = 1
while q:
    a = q.popleft()
    for i in g[a]:
        if v[i] == 0:
            n[i] = n[a] + 1
            q.append(i)
            v[i] = 1
return sum(num)
의 느낌으로 bfs를 진행할 수 있다. 
"""
