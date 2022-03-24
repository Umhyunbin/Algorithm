def solution(citations):
    c = sorted(citations, reverse = True)
    less = min(c[0], len(c))
    for i in range(less, 0, -1):
        cnt = 0
        for j in c:
            if i <= j:
                cnt += 1
            else:
                break
        if cnt >= i:
            return i
    else:
        return 0

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""