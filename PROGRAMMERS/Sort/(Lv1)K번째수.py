def solution(array, commands):
    answer = []
    for i in commands:
        s = sorted(array[i[0] - 1: i[1]])
        answer.append(s[i[2] - 1])
    
    return answer

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""