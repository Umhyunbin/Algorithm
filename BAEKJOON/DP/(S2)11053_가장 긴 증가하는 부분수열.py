import sys

input = sys.stdin.readline
N = int(input())
li = list(map(int, input().rstrip().split()))

dp = [0] * N
for i in range(N):
    for j in range(i):
        if li[j] < li[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

"""
자기 자신보다 앞쪽을 쭉 보면서,
자기 자신보다 숫자가 작으면서 가장 큰 원소 개수 가지는 것을 찾아
+ 1 처리(자기 자신까지) """
