import sys

def recursion(n, s):
    x, y = s
    standard = paper[x][y]
    temp = {-1 : 0, 0 : 0, 1 : 0}
    flag, t_flag = True, True
    
    for i in range(x, x + n):        
        for j in range(y, y + n):            
            if paper[i][j] != standard:
                t_flag = False
                break
        if not t_flag:
            flag = False
            break
            
    if flag:
        d[standard] += 1
        return
    elif n > 3:
        num = n // 3
        for i in range(3):
            for j in range(3):
                recursion(num, (x + num * i, y + num * j))
    else:
        for i in range(x, x + n):
            for j in range(y, y + n):            
                d[paper[i][j]] += 1
        return
                
                

input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().rstrip().split())) for _ in range(N)]
d = {-1 : 0, 0 : 0, 1 : 0}

recursion(N, (0, 0))
print(d[-1], d[0], d[1], sep = '\n')

"""
N의 크기와 시작 탐색 위치를 인자로 가지는 recursion 함수를 생각하였다.
N * N 을 탐색하는 동안 값이 모두 같아야 하나의 종이로 인정할 수 있으므로
flag를 이용하여 다른 것이 있는지 체크한다.

다 같다면 하나의 종이이므로 더 이상 분할을 진행하지 않고 종이 개수 += 1.
그렇지 않은 상황이라면 N의 크기를 따진다.

N > 3 이라면 더 작은 단위에서 볼 필요가 있으므로 시작 위치, N 크기 지정하여
recursion 재귀를 돌리고,
N == 3 이라면 더 쪼갤 필요가 없으므로 바로 dict에 개수를 추가해준다.
"""