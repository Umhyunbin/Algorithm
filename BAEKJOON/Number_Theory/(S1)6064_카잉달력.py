import sys

T = int(input())
for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    flag = True

    while (x <= M * N):
        if x % N == y % N:
            print(x)
            flag = False
            break
        x += M
    if flag:
        print(-1)