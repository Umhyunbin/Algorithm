import sys
from math import inf
import heapq

def dijkstra(g, k):
    d = [inf] * (V + 1)
    q = []
    heapq.heappush(q, (0, k))
    d[k] = 0
    while q:
        dist, node = heapq.heappop(q)
        if d[node] < dist:
            continue
        for i in g[node]:
            c = dist + i[1]
            if c < d[i[0]]:
                d[i[0]] = c
                heapq.heappush(q, (c, i[0]))
    return d

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
K = int(input())
g = [[] for _ in range(V + 1)]

for i in range(E):    
    u, v, w = map(int, input().rstrip().split())
    g[u].append((v, w))

answer = dijkstra(g, K)
for i in range(1, V + 1):
    print(answer[i]) if answer[i] < inf else print("INF")

"""
g -> 1 ~ V 각각에 u -> v로 가는 가중치 w를 추가해준다.
d -> 시작 지점부터 각 노드까지의 최단 거리를 저장.

다익스트라 알고리즘에서 원래 매번 최단 거리인 node를 골라야하는데
heapq를 사용하면 O(lgN) 정도로 pop시킬 수 있다.

heapq에는 (시작 노드로 가기 위한 최단 거리, 노드) 로 들어가 있다.
자기 자신은 거리 0으로 설정해준다. (d[k] = 0)

매번 dist(시작 노드까지 갈 수 있는 최단 거리), node(현재 기준 노드)를 꺼내어
현재 기존 최단 거리가 이미 더 작은 상태면 갱신이 필요 없으므로 continue.

g[node] -> node와 인접한 노드, 가중치가 저장되어있음.
이를 순회하면서 node에서 인접한 노드까지의 거리(i[1]), dist(시작노드 ~ node거리)
-> 시작 노드부터 node와 인접한 노드까지의 거리 를 c라고 정의하고,
만약 이 c가 원래 d에 저장되어있는 인접노드까지의 거리(d[i[0]])보다 작으면
거리를 c로 갱신하고 heapq에 추가해준다.
(c가 더 크면 기존 루트를 유지하는 것이 더 최단 경로이다.)
"""