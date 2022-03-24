def solution(numbers):     
    return str(int(''.join(sorted(list(map(str, numbers)), key = lambda x : x*3, reverse = True))))

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""