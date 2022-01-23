import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    st = []
    n = int(input())
    st.append(list(map(int, input().split())))
    st.append(list(map(int, input().split())))
            
    for j in range(1, n):
        if j == 1:
            st[0][j] += st[1][j - 1]
            st[1][j] += st[0][j - 1]
        else:
            st[0][j] += max(st[1][j - 1], st[1][j - 2])
            st[1][j] += max(st[0][j - 1], st[0][j - 2])
    print(max(st[0][n - 1], st[1][n - 1]))
    

"""
a1 a2 a3
a4 a5 a6
1  2  3

ex) 3번째를 하고 싶다.
a3 입장에서는 a1 + a5, a4 중 큰거랑 더하면 된다.
a6 입장에서는 a2 + a4, a1 중 큰거랑 더하면 된다.
이를 st배열에 그대로 더해주면서 이전 값들의 합을 자연스럽게 기억함.
"""
