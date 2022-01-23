import sys

input = sys.stdin.readline
N = int(input())
li = [list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    li[i][0] += min(li[i - 1][1], li[i - 1][2])
    li[i][1] += min(li[i - 1][0], li[i - 1][2])
    li[i][2] += min(li[i - 1][0], li[i - 1][1])
print(min(li[N - 1]))
