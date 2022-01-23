import sys

input = sys.stdin.readline
cnt = int(input())
score = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(cnt):
    score[i] = int(input())
    
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, cnt):
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])
print(dp[cnt - 1])

"""
한 계단 or 두 계단 오를 수 있는데 연속된 세 개의 계단을 모두 밟으면 안됨.
i번째 입장에서는 i-2번째에서 2 계단을 오르거나,
                 i-3번째에서 i-1번째로 넘어오고 i번째로 오는 경우가 있다.
"""
