def solution(n, words):
    # 탈락하는 경우 : 글자 불일치 / 중복 단어
    duplicate_set = set()
    for i, v in enumerate(words):
        if not i:
            duplicate_set.add(v)
            continue
        if v in duplicate_set or words[i - 1][-1] != v[0]:
            return [(i + 1) % n if (i + 1) % n > 0 else n, i // n + 1]
        duplicate_set.add(v)
    
    return [0, 0]

