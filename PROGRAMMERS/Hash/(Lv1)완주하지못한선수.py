def solution(participant, completion):
    d = {}
    for i in participant:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in completion:
        d[i] -= 1
    for i in d:
        if d[i] == 1:
            return i

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""