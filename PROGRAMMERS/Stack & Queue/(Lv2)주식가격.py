from collections import deque

# 처음 풀은 방법(queue)
def solution_queue(prices):
    answer = []
    p = deque(prices)
    n = len(p)

    for i in range(n - 1):
        num = p.popleft()
        cnt = 0
        for j in range(i + 1, n):            
            cnt += 1
            if num > prices[j]:
                break   
        answer.append(cnt)
    answer.append(0)
    return answer

"""
큐를 이용한 이중 반복문.
더 작은 값이 있으면 break하는 방법.
"""
# 더 좋다고 알려진 풀이(stack)
def solution_stack(prices):
    length = len(prices)
    answer = [i for i in range(length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

"""
기본적으로 끝까지 안떨어진다는 default 배열 -> answer.
stack -> 아직 처음으로 가격 떨어지는 시간대가 정해지지 않은 시간대 stack.
stack 안의 시간들은 자신이 언제 처음으로 떨어지는지 기다리고 있다고 생각.
그래서 반복문이 진행될 때마다 하나씩 stack[-1]부터 확인하면서 떨어졌는지 확인.

만약 stack[-1]보다 더 큰 값이면
당연히 stack[-2], stack[-3]... 들보다도 큰 값일 것이다.
(stack 안의 시간들은 아직 떨어짐을 경험하지 못한 값들이기 때문에
순서간의 대소관계가 있다.
ex) stack = [1, 2, 3] -> 다음에 4가 있다고 생각해보자.
stack[-1] = 3인데 그거보다 4가 크므로 아직 작아지지 않음.
3보다도 큰 4이기 때문에 1, 2 입장에선 당연히 아직 작아지지 않는 상태.

ex) stack = [1, 2, 3, 4], 다음에 2가 있다고 생각해보자.
4 > 2 -> answer[4] = 5 - 4 (stack 안의 시간, 현재 비교군 시간 차이를 의미)
3 > 2 -> answer[3] = 5 - 3
.

i초일때는 i+1초부터 떨어지는 것을 확인할 수 있으므로
i번째일 때 stack에 append.

"""

prices = [1, 2, 3, 2, 3]
print(solution_queue(prices))
print(solution_stack(prices))

"""
주식가격이 몇 초동안 떨어지지 않고 유지되는지 계산하는 문제.
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""
