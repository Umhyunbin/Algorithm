from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        li = []
        for order in orders:
            comb = list(combinations(order, c))
            comb = list(map(lambda x: "".join(sorted(x)), comb))
            li += comb
        count = Counter(li).most_common()
        
        if len(count) > 0 and count[0][1] > 1:
            max_num = count[0][1]
            for cnt in count:
                if cnt[1] < max_num:
                    break
                answer.append(cnt[0])
            answer.sort()
             
    return answer

"""
모든 조합을 구하고 각 값을 정렬함("XY", "YX"는 같은 코스)
-> Counter를 이용하여 각 원소별 개수를 구한 뒤, most_common을 이용하여 높은 숫자부터 정렬
count가 2 이상이면서 원소가 존재하는 경우에 가장 큰 값을 기록한 원소들을 append
마지막에 오름차순 정렬
"""
