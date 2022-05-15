def solution(s):
    answer = ''
    for i, w in enumerate(s):
        if w == ' ':
            answer += w
            continue
        if i == 0:
            if not w.isalpha() or w.isupper():
                pass
            else:
                w = w.upper()
            answer += w
        else:
            if s[i - 1] == ' ':
                if not w.isalpha() or w.isupper():
                    pass
                else:
                    w = w.upper()
            else:
                w = w.lower()
            answer += w
    return answer
