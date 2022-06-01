def gcd(a, b):
    """
    유클리드 호제법
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def solution(w,h):
    """
    1. w, h가 서로소가 되게 gcd로 나누어준다.
    (자르는 선이 정확히 격자점을 지날때의 최소 단위 * gcd만큼 반복)
    ex) 8 * 12 -> 2 * 3 에서 정확히 격자점 지남, 패턴이 gcd(8, 12) = 4 만큼 반복
    
    2. w, h가 서로소인 상태에서,
    선과 만나는 사각형 개수는 w + h - 1(ㄱ자 모양으로 간다고 생각)
    """
    answer = 1
    m, M = min(w, h), max(w, h)
    g = gcd(w, h)
    
    return w * h - (h // g + w // g - 1) * g           
                
