from collections import deque
import sys

def dfs(g, v):
    visited = []
    s = [v]
    
    while s:
        p = s.pop()
        if p not in visited:
            visited.append(p)
            if p in g:                
                tmp = list(g.get(p) - set(visited))
                tmp.sort(reverse = True)
                s += tmp
            
    return visited

def bfs(g, v):
    visited = []
    q = deque([v])
    
    while q:
        p = q.popleft()
        if p not in visited:
            visited.append(p)
            if p in g:                
                tmp = list(g.get(p) - set(visited))
                tmp.sort()  # 작은것 부터 방문.
                q += tmp
            
    return visited

N, M, V = map(int, sys.stdin.readline().strip().split())
li = []
for _ in range(M):
    li.append(list(map(int, sys.stdin.readline().strip().split())))

graph = {}
for i in li:
    # 양 방향 다 가능하므로 쌍으로 추가. 
    if i[0] not in graph:
        graph[i[0]] = {i[1]}
    else:
        graph[i[0]].add(i[1])

    if i[1] not in graph:
        graph[i[1]] = {i[0]}
    else:
        graph[i[1]].add(i[0])
        
d = dfs(graph, V)
b = bfs(graph, V)

for i in d:
    print(i, end=' ')
print()
for i in b:
    print(i, end=' ')

"""
그래프 관계를 dict로 표현했을 때의
dfs, bfs 구
"""
