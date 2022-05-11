from collections import deque

def solution(n, results):
    answer = 0
    rank = [[0] * n for _ in range(n)]
    
    for r in results:
        rank[r[0] - 1][r[1] - 1] = 2 # win
        rank[r[1] - 1][r[0] - 1] = 1 # lose

    q = deque(results[:])   
    while q:
        tmp = []
        # r = [win_num, lose_num]
        r = q.popleft()
        # lose_num이 이긴 숫자가 있으면 win_num도 그 숫자를 이겼다고 표시
        # ex: [4, 2], [2, 5] -> [4, 5]도 성립해야 함
        for i, j in enumerate(rank[r[1] - 1]):
            if j == 2 and rank[r[0] - 1][i] == 0:
                rank[r[0] - 1][i] = 2
                rank[i][r[0] - 1] = 1
                # 이긴 것으로 새로 처리되었기 때문에 탐색 필요
                q.append([r[0], i + 1]) 
                
    for r in rank:
        # 자기 자신빼고는 전부 0이 아니어야 순위를 알고 있는 상태
        if r.count(0) == 1:
            answer += 1
        
    return answer
