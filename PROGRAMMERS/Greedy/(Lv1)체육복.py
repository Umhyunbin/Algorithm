def solution(n, lost, reserve):
    s_reserve = sorted(list(set(reserve) - set(lost)))
    s_lost = sorted(list(set(lost) - set(reserve)))
    
    for r in s_reserve:
        if r - 1 in s_lost:
            s_lost.remove(r - 1)
        elif r + 1 in s_lost:            
            s_lost.remove(r + 1)          
                    
    return n - len(s_lost)

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges