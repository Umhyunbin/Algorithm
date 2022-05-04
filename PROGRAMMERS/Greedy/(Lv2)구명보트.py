from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        if len(people) == 1:
            answer += 1
            break
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.pop()
        answer += 1
    
    return answer

"""
가장 작은 원소, 큰 원소를 비교하여 limit 넘기면 큰 원소만 보내고,
limit 안넘기면 둘 다 보내는 느낌으로 진행.
"""
