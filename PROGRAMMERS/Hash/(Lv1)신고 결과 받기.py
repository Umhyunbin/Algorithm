from collections import defaultdict

def solution(id_list, report, k):
    """
    person : 유저별 신고 유저 set
    attack_num : 유저별 신고당한 횟수
    
    처음 신고하는 경우면 신고유저 추가, 신고횟수 증가
    각 유저별로 신고한 유저 set 돌면서 해당 유저 신고횟수가 k 이상이면 +1
    """
    person = defaultdict(set)
    attack_num = defaultdict(int)
    answer = [0] * len(id_list)
    
    for r in report:
        li = r.split()
        r1, r2 = li[0], li[1]        
        if r2 not in person[r1]:
            attack_num[r2] += 1
            person[r1].add(r2)
    
    for idx, v in enumerate(id_list):
        for i, p in enumerate(person[v]):        
            if attack_num[p] >= k:
                answer[idx] += 1
    
    return answer
