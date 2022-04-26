def solution(lottos, win_nums):
    score, iszero = 0, 0
    answer = []
    for i in lottos:
        if i == 0:
            iszero += 1
        elif i in win_nums:
            score += 1
    min_rank = min(6, 7 - score)
    max_rank = max(1, min_rank - iszero)
    answer = [max_rank, min_rank]
    return answer
