import sys
from collections import deque

def bfs(g, n):
    v = []    
    q = deque(list(g.get(n)))  # n에서 인접한 노드들을 시작으로 함.    
    while q:
        p = q.popleft()
        if p not in v:
            v.append(p)
            if p in g:
                tmp = list(g.get(p) - set(v))                
                q += tmp        
    return v


N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

d = {}
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            if i in d:
                d[i].add(j)
            else:
                d[i] = {j}

result = []
for i in range(N):
    if i in d:
        b = bfs(d, i)
        result.append([1 if k in b else 0 for k in range(N)])
    else:
        result.append([0 for _ in range(N)])

for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ')
    print()
    
"""
여기서 g는 dict형태가 아닌 인접행렬 형태라고 가정하자.
v = [0] * N
q = deque([n])
while q:
    p = q.popleft()
    for i, j in enumerate(g[p]):  
        if v[i] == 0 and j == 1:    -> 방문하지 않았고 연결되어 있다면
            v[i] = 1
            q.append(i)
return v

이렇게 bfs를 처리해주면 dict 형태로 굳이 만들지 않아도 괜찮았다.
Floyd_Warshall 알고리즘으로도 해결할 수 있지만
가중치그래프가 아니라 시간복잡도를 위해 bfs를 이용하였다.
"""
