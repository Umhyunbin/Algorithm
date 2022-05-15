from itertools import product

def solution(word):
    li = []
    mo = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        li += list(map(lambda x: "".join(x), product(mo, repeat = i)))
    li.sort()
    return li.index(word) + 1
