def solution(m, n, puddles):
    up = [0 for _ in range(m)]
    
    for i in range(n):
        down = [0 for _ in range(m)]
        for j in range(m):
            if i == 0:
                if j == 0:
                    down[j] = 1
                elif [j + 1, i + 1] not in puddles:
                    down[j] = down[j - 1]                
            else:
                if j == 0:
                    if [j + 1, i + 1] not in puddles:
                        down[j] = up[j]
                elif [j + 1, i + 1] not in puddles:
                    down[j] = down[j - 1] + up[j]                
        up = down.copy()
        
    return up[m - 1] % 1000000007

"""
up, down 두 개의 배열을 이용해 현재 줄(down)을 계산.
웅덩이 자리는 무조건 0이므로 웅덩이에 해당하지 않을때만 이전 경로 고려.
문제에서 열, 행 순서이고 인덱스가 1부터 시작하여 puddle 값을 [j + 1, i + 1]로 설정.
"""
# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges