from collections import deque
import sys

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

N = int(input())
M = int(input())
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
        
b = bfs(graph, 1)
print(len(b) - 1)

"""
바이러스 걸리는 다른 컴퓨터 수 출력하기.
각 노드간 연결관계를 주었기 때문에 dict 형태로 표현.

bfs로 해결하였고 자기자신을 제외해야 하기 때문에 1을 뺌.
"""
