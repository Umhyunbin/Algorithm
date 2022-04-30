from collections import defaultdict

def solution(N, stages):
    answer = []
    d = defaultdict(int)
    num = len(stages)
    for s in stages:
        d[s] += 1
    # 작은 스테이지부터 확인하기 위해 정렬
    d = dict(sorted(d.items(), key = lambda x: x[0]))
    ans = {}
    
    # d[i] : 현재 도전 위치, num : 총 도전자 수
    for i in d.keys():
        if i <= N:            
            ans[i] = d[i] / num
            num -= d[i]
    
    # 실패율 내림차순, 같은 실패율일 경우 작은 번호부터.
    tmp = sorted(ans.items(), key = lambda x: (-x[1], x[0]))
    answer = []
    for a in tmp:
        answer.append(a[0])
    
    # stage list에 없는 값 추가.
    for i in range(1, N + 1):
        if i not in answer:
            answer.append(i)
    return answer

