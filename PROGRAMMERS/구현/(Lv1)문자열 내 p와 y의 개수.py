def solution(s):
    answer = 0
    s = s.lower()
    for i in s:
        if i == 'p':
            answer += 1
        elif i == 'y':
            answer -= 1
    return True if answer == 0 else False
