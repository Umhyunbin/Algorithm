import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * 1001
dp[0], dp[1], dp[2] = 0, 1, 3

for i in range(3, n + 1):
    dp[i] = sum([dp[i - 2] * 2, dp[i - 1]])
print(dp[n] % 10007)

"""
i번째 입장에서 i - 2번째에서 올 수 있는 방법은 ㅁ, = 2가지,
               i - 1번째에서 올 수 있는 방법은 | 1가지이다.
따라서 sum([dp[i - 2] * 2, dp[i - 1]])으로 진행.
"""
