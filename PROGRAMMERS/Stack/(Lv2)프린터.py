from collections import deque

def solution(priorities, location):
    answer = 0
    p = deque(priorities)
    while p:
        f = p.popleft()
        flag = True
        for i in range(len(p)):
            if f < p[i]:
                flag = False
                break
        if flag:
            answer += 1
            if location == 0:
                break
        else:
            p.append(f)
        
        location = (location - 1) % len(p)
    return answer

pr = [2, 1, 3, 2]
loc = 2
#pr = [1, 1, 9, 1, 1, 1]
#loc = 0
print(solution(pr, loc))
