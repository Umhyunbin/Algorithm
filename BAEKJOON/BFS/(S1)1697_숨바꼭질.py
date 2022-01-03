from collections import deque

N, K = map(int, input().split())

d = deque()
d.append(N)
dist = [0] * 100001

while d:     
    n = d.popleft()    
    if n == K:
        print(dist[n])
        break
    for x in (n-1, n+1, n*2):
        if 0 <= x <= 100000 and not dist[x]:
            dist[x] = dist[n] + 1
            d.append(x)

"""
X 위치에서 1초 후 X-1, X+1, 2X 중 하나로 이동 가능.
N -> K를 찾아야 함.

3가지 각각에 대해 x 범위 안에 있고 아직 조사하지 않은 값이면
1을 더하고 d에 append 해주어 탐색을 이어나갈 수 있도록 한다. 
"""
