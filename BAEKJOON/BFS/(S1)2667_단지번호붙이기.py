import sys
from collections import deque

def bfs(g, loc):
   
    result = [] 
    for i in range(N):
        for j in range(N):            
            if g[i][j] == 1:
                q = deque([[i, j]])
                g[i][j] = 0
                cnt = 0
                while q:       
                    coord = q.pop()
                    x, y = coord[0], coord[1]                    
                    
                    if x < N - 1 and g[x + 1][y] == 1:
                        g[x + 1][y] = 0
                        q.append([x + 1, y])                            
                    if x > 0 and g[x - 1][y] == 1:
                        g[x - 1][y] = 0
                        q.append([x - 1, y])                            
                    if y < N - 1 and g[x][y + 1] == 1:
                        g[x][y + 1] = 0
                        q.append([x, y + 1])                            
                    if y > 0 and g[x][y - 1] == 1:
                        g[x][y - 1] = 0
                        q.append([x, y - 1])
                    cnt += 1  
                result.append(cnt)
                            
    return result
                

N = int(sys.stdin.readline().rstrip())
m = []
loc = []
for i in range(N):
    tmp = [int(j) for j in sys.stdin.readline().rstrip()]
    for k in range(len(tmp)):
        if tmp[k] == 1:
            loc.append([i, k])
    m.append(tmp)

r = sorted(bfs(m, loc))

print(len(r))
for i in r:
    print(i)

"""
단지마다 번호를 매기어 몇 단지로 구성되어 있는지, 집 수는 어떤지 조사해야함.

탐색이 끝난 좌표에 대해서는 0 처리를 해주어 탐색을 진행하지 않게 설정 가능.
어차피 while문은 인접한 원소 수만큼 돌기 때문에 bfs를 써도 상관은 없는 문제이다.

한 좌표 기준 사방으로 추가해야 할 값을 q에 추가하고,
while문이 한 번 진행될 때마다 인접원소가 존재한다는 뜻이므로 cnt += 1을 해준다.
"""
