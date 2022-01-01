from collections import deque

def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)
    
    while p:        
        p = deque([p[i] + s[i] for i in range(len(p))])
        
        if p[0] == 100:
            cnt = 0
            while p and p[0] >= 100:
                p.popleft()
                s.popleft()
                cnt += 1
                
            answer.append(cnt)
    return answer
p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]

print(solution(p, s))
    
"""
배포되어어야 하는 순서대로 작업의 진도가 적힌 정수배열 p
각 작업별 속도 s

맨 앞 작업이 100 이상(진도율)되면 배포.
이 때, 뒤의 것에서 이미 진도율 100 이상 있으면 같이 배포.
이렇게 한 번 배포할 때 몇 개씩 배포하는지 answer 로 추출.

출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
"""
