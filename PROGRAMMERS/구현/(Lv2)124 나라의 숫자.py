def solution(n):
    """
    작은 자리수부터 보아도 나머지 입장에서 큰 문제가 없
    """
    answer = ''
    li = ['4', '1', '2']
    while n > 0:
        r = n % 3
        answer = li[r] + answer
        if r == 0:
            n = (n - 1) // 3
        else:
            n //= 3
            
    return answer
