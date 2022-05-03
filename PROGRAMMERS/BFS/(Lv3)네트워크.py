from collections import defaultdict
from collections import deque

def bfs(g, v):
    visited = []
    q = deque([v])
    
    while q:
        p = q.popleft()
        if p not in visited:
            visited.append(p)
            if p in g:
                tmp = list(g.get(p) - set(visited))
                q += tmp
    return visited

def solution(n, computers):
    d = defaultdict(set)

    # 연결 관계를 dict로 표현
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                d[i].add(j)
    
    vertex = list(range(n))
    answer = 0
    while vertex:
        p = vertex.pop()
        # p와 연결되어 있는 노드들을 반환하여 vertex에서 제거
        s = bfs(d, p)
        vertex = list(set(vertex) - set(s))
        answer += 1
    return answer
