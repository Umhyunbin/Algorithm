import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())    
        
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        arr = deque()
    
    isR = 0
    flag = True
    
    for j in p:
        if j == 'R':
            isR += 1
        elif j == 'D':
            if len(arr) > 0:
                if isR % 2 == 0:                    
                    arr.popleft()
                else:                    
                    arr.pop()
            else:
                print("error")
                flag = False
                break
    if flag:       
        if isR % 2 == 0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')

"""
R : reverse
D : delete first number

매번 reverse 하는 것은 시간 복잡도 증가.
R 명령이 홀수 / 짝수 인지에 따라 달라짐.

pop, popleft를 구분함으로써 reverse한 다음 popleft하는 효과를 볼 수 있음.
"""
