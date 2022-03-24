def solution(brown, yellow):
    half = brown // 2
    i, j = half - 2, 2
    while i >= 1 or j <= half:
        if (i - 1) * (j - 1) == yellow:
            break
        i -= 1
        j += 1
    
    answer = [i + 1, j + 1]
    return answer

"""
aaaa
abba
aaaa 라고 해보자.

brown -> a의 개수.
half가 의미하는 것 -> c + d. c를 가로, d를 세로라고 생각해보자. 
aaaa
abbd
cccd

yellow는 (n(c) - 1) * (n(d) - 1)로 형성될 것이다.
따라서 가로가 가장 긴 경우(yellow의 세로길이가 1인 경우)부터 완전탐색을 통해
정답을 찾아나간다.
"""

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""