
from collections import deque
from collections import defaultdict

def bfs(g, n, v):
    visited = [-1] * (n + 1)
    distance = 1
    q = deque([(v, distance)])
    check = set()

    while q:
        p, distance = q.popleft()
        if visited[p] == -1:
            visited[p] = distance
            distance += 1
            check.add(p)
            if p in g:
                tmp = list(g.get(p) - check)
                for e in tmp:
                    q.append((e, distance))
    return visited
                

def solution(n, edge):
    d = defaultdict(set)
    for i in range(len(edge)):
        e = edge[i]
        d[e[0]].add(e[1])
        d[e[1]].add(e[0])
    answer = bfs(d, n, 1)
        
    return answer.count(max(answer))
