def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    """
    Kruskal Algorithm
    """
    # 부모 테이블
    parent = list(range(n))
    
    # 가중치 기준으로 정렬
    costs = sorted(costs, key = lambda x: x[2])
    
    answer = 0
    for i in range(len(costs)):
        a, b, c = costs[i]
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c

    return answer
