def solution(num):
    answer = 0
    if num == 1:
        return answer
    while answer <= 500:
        num = num * 3 + 1 if num % 2 == 1 else num // 2
        answer += 1
        if num == 1:
            return answer
    return -1
