def solution(routes):
    """
    전출 지점 기준 정렬 
    -> routes[i][0]과 현재 camera를 비교
    -> camera가 더 큰 값이면 routes[i]는 무조건 camera에 잡힘
    (전출 지점 기준 정렬이기 때문에 전입지점이 camera보다 작으면 무조건 camera 지남)
    """
    answer = 0
    camera = -30001
    routes = sorted(routes, key = lambda x: x[1])
    
    for r in routes:
        if camera < r[0]:
            answer += 1
            camera = r[1]
            
    return answer
