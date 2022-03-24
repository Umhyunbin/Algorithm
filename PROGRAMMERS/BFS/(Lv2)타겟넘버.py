from collections import deque

def solution(numbers, target):
    q = deque([0])
    for n in numbers:
        temp = deque([])
        while q:
            elm = q.popleft()
            temp.append(elm + n)
            temp.append(elm - n)
        q = temp
    return q.count(target)

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges