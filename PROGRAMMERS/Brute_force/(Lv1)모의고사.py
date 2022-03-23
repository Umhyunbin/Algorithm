def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    d = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            d[0] += 1
        if answers[i] == two[i % len(two)]:
            d[1] += 1
        if answers[i] == three[i % len(three)]:
            d[2] += 1
    
    max_val = max(d)
    result = []
    for i in range(len(d)):
        if d[i] == max_val:
            result.append(i + 1)
    return result

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""