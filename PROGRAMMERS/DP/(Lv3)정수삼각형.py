def solution(triangle):
    # initial value
    li = [triangle[0][0]]
    for i in range(1, len(triangle)):
        temp = triangle[i]
        for j in range(len(temp)):
            if j == 0:
                temp[j] += li[j]
            elif j == len(temp) - 1:
                temp[j] += li[j - 1]
            else:
                temp[j] += max(li[j - 1], li[j])
        li = temp.copy()        
    return max(li)

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges