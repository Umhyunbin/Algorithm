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

N, M = map(int, sys.stdin.readline().strip().split())
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
        
vertex = list(range(1, N + 1))
count = 0
while True:
    v = vertex.pop()
    b = bfs(graph, v)
    vertex = list(set(vertex) - set(b))
    count += 1
    if len(vertex) == 0:
        break
print(count)


"""
그래프 연결 요소의 개수를 구하는 문제.

한 노드에 대해 연결되어있는 노드를 bfs를 통해 반환하고,
이를 전체 vertex list에서 제거하는 방식으로 개수를 센다.
"""
