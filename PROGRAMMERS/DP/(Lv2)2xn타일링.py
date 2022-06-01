def solution(n):
    """
    dp[i - 2]에서 가로로 쌓아서 2개 채우기
    dp[i - 1]에서 세로로 쌓아서 1개 채우기
    이렇게 2가지는 절대 겹치지 않으면서 모든 방법을 채움
    -> dp[i] = dp[i - 2] + dp[i - 1]
    """
    dp = [0] * 60001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
    return dp[n]
                
