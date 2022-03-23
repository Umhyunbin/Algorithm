import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

count = 0
for i in range(n - 1, -1, -1):
    count += k // coins[i]
    k %= coins[i]

print(count)