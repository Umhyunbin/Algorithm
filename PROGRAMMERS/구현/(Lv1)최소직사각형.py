def solution(sizes):
    """
    1. 각 명함의 대소관계를 통일시킨다.
    2. A = [a1, a2, ...] B = [b1, b2, ...] 이고 명함 = [ai, bi]라면,
    max(A), max(B)를 곱한 값이 정답이다.
    """
    sizes = list(map(sorted, sizes))
    maxw, maxh = 0, 0
    for i in sizes:
        if maxw < i[0]:
            maxw = i[0]
        if maxh < i[1]:
            maxh = i[1]
    return maxw * maxh

"""
max(max(x) for x in sizes) * max(min(x) for x in sizes)
이 풀이도 같은 접근이다.
"""
