def solution(money):
    N = len(money)
    
    # 무조건 첫 번째 선택
    dp1 = [0] * N
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])
    
    # 무조건 마지막 선택
    dp2 = [0] * N
    dp2[0], dp2[1] = 0, money[1]   
    for i in range(2, N):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])
    
    # dp1은 마지막 선택을 안하므로 N - 2, dp2는 마지막을 선택하므로 N - 1번째를 봐야함.
    return max(dp1[N - 2], dp2[N - 1])

"""
집들이 원모양으로 배치되어있기에 시작 포인트의 양 옆을 봐야함 
-> 첫 번째에서 시작하면 N 번째는 무조건 제외해야 함 !
-> 그 두 가지 경우를 나누어 해결
"""
