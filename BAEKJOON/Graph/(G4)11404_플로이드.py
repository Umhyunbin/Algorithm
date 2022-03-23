import sys
from math import inf

input = sys.stdin.readline
n = int(input())
m = int(input())
v = [[inf] * n for _ in range(n)]
for i in range(n):
    v[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    if c < v[a - 1][b - 1]:
        v[a - 1][b - 1] = c
    
for k in range(n):
    for i in range(n):
        for j in range(n):            
            if v[i][k] + v[k][j] < v[i][j]:
                v[i][j] = v[i][k] + v[k][j]

for i in range(n):
    for j in range(n):        
        print(v[i][j], end = ' ') if v[i][j] < inf else print(0, end = ' ')       
    print()