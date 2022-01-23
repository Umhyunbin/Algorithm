import sys

input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            li[i][j] += li[i - 1][j]
        elif j == i:
            li[i][j] += li[i - 1][j - 1]
        else:
            li[i][j] += max(li[i - 1][j - 1], li[i - 1][j])
            
print(max(li[n - 1]))

"""
합을 계속 누적하면서 진행.
양 끝은 선택지가 없으므로 그대로 내려오고,
나머지는 위의 2개중에 큰 것을 선택.
"""
