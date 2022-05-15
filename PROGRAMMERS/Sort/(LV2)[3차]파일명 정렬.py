from collections import defaultdict
import re

def solution(files):
    answer = []
    d = defaultdict(list)
    for i, v in enumerate(files):
        # d = {main : [head, number, index], ...}
        # sorted by head, number, index        
        number = re.search(r"\d+", v).group()
        head = v.split(number)[0]
        d[v] = [head.lower(), int(number), i]
    d_sort = sorted(d.items(), key = lambda x: [x[1][0], x[1][1], x[1][2]])
    return list(map(lambda x: x[0], d_sort))
