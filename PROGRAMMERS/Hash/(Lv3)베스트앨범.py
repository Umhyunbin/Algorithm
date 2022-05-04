from collections import defaultdict

def solution(genres, plays):
    answer = []
    # total : 장르별 재생 횟수 / detail : 장르별 고유 번호, 재생 횟수
    total = defaultdict(int)
    detail = defaultdict(list)
    
    for i in range(len(plays)):
        total[genres[i]] += plays[i]
        detail[genres[i]].append([i, plays[i]])
    
    # 1. 속한 노래가 많이 재생된 장르(내림차순)
    t = dict(sorted(total.items(), key = lambda x: x[1], reverse = True))
    for g in t.keys():
        aim = detail[g]
        # 2. 장르 내에서 많이 재생된 노래(내림차순), 재생 횟수 같으면 고유 번호 낮은 노래(오름차순)
        result = sorted(aim, key = lambda x: (-x[1], x[0]))
        
        # 장르에 속한 곡이 1개 -> 1개의 고유 번호만 선택
        if len(result) == 1:
            answer += [result[0][0]]
        elif len(result) >= 2:
            answer += [result[0][0], result[1][0]]
                        
    return answer
