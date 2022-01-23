import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for i in range(T):    
    A, B = map(int, input().rstrip().split())
    find = [0] * 10000
    find[A] = 1
    q = deque([(A, "")])
    while q:
        p, m = q.popleft()
        
        D_val = (p * 2) % 10000       
        S_val = (p + 9999) % 10000
        L_val = (p % 1000) * 10 + p // 1000
        R_val = (p % 10) * 1000 + p // 10

        if D_val == B:
            print(m + "D")
            break
        elif not find[D_val]:
            find[D_val] = 1            
            q.append((D_val, m + "D"))
            
        if S_val == B:
            print(m + "S")
            break
        elif not find[S_val]:
            find[S_val] = 1            
            q.append((S_val, m + "S"))
            
        if L_val == B:
            print(m + "L")
            break
        elif not find[L_val]:
            find[L_val] = 1            
            q.append((L_val, m + "L"))
            
        if R_val == B:
            print(m + "R")
            break
        elif not find[R_val]:
            find[R_val] = 1            
            q.append((R_val, m + "R"))

"""
DSLR에 맞는 값들을 각각 구한 뒤,
B와 같으면 끝내고, 그렇지 않고 아직 find에 없으면(아직 안한 값)
탐색한 값이라고 한 다음, 그 값과 명령연산을 추가하는 작업 진행.
"""
