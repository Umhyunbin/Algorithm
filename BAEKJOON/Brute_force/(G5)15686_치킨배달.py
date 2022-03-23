import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
li = [list(map(int, input().rstrip().split())) for _ in range(N)]

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if li[i][j] == 1:
            house.append([i, j])
        elif li[i][j] == 2:
            chicken.append([i, j])

p = list(combinations(range(len(chicken)), M))
distance = [0] * len(p)
for i in range(len(house)):
    r1, c1 = house[i][0], house[i][1]    
    for j in range(len(p)):
        tmp = []
        for k in p[j]:
            r2, c2 = chicken[k]
            tmp.append(abs(r1 - r2) + abs(c1 - c2))
        distance[j] += min(tmp)
print(min(distance))
        
        
"""
1. 치킨집과 일반집의 좌표를 받는다.
2. 치킨집에 대한 조합을 찾는다.
3. 일반 집에 대하여 치킨 집 조합에 해당하는 치킨 집들과의 거리를 산출한 뒤,
그 중 최소값을 distance[치킨집 조합의 index]에 더해준다.
4. 최종 최소값이 정답.

ex) 치킨집 : 4개, M = 2
-> 6가지의 치킨집 조합 후보군이 생긴다.
치킨집1 : (0, 0)
치킨집2 : (1, 2)
일반집 : (0, 1)
이라면 거리 -> min(1, 2) = 1이 되어 1이 해당 조합 값에 더해지는 방식으로 진행.
"""