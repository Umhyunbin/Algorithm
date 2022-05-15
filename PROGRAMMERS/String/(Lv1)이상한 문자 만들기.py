def solution(s):
    answer = ''
    idx = 0
    for i, w in enumerate(s):
        if w == ' ':
            answer += w
            continue
        elif i == 0:
            answer += w.upper()
            idx += 1
        else:
            if s[i - 1] == ' ':
                idx = 0
            w = w.upper() if idx % 2 == 0 else w.lower()
            answer += w
            idx += 1
    return answer
