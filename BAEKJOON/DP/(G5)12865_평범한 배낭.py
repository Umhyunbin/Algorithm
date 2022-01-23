import sys

input = sys.stdin.readline
N, K = map(int, input().split())
li = [map(int, input().split()) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    w, v = li[i - 1]    
    for j in range(K + 1):        
        if w <= j:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][K])
    
"""
DP[i][j] -> 처음 i개의 물건, j의 무게를 감당할 수 있는 상태.
ex) 무게 6, 가치 13
>>> DP[3][7] = max(DP[2][7], 13 + DP[2][7 - 6])
-> 2까지는 진행이 되었고, 3까지 볼 때의 최대를 보고 싶다.
-> 물건 2개, 남은 무게 7 / 13(물건 가치) + 7 - 6 = 1의 무게를 더 넣을 수 있음.
"""
