from itertools import permutations

def solution(numbers):
    num_list = [n for n in numbers]
    p_list = []
    
    # iterate for all permutation number. i.e. 3P1, 3P2, ...
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(num_list, i))        
        for j in temp:
            num = int("".join(j))
            # 0, 1 -> not prime
            if num >= 2:
                p_list.append(num)

    del temp
    del num_list

    p_list = set(p_list)    
    answer = 0
    for p in p_list:
        flag = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                flag = False
        if flag:
            answer += 1
    
    return answer

# 7, 17, 71 -> 3
print(solution("17")) 
# 11, 101
print(solution("011"))

"""
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
"""

"""
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""