import sys

input = sys.stdin.readline
M = int(input())

answer = 0
for i in range(M):
    N, S = map(int, input().rstrip().split())
    b = 1000000005
    x = 1
    while b:
        if b & 1:
            x = (x * N) % 1000000007
        N = (N * N) % 1000000007
        b = b >> 1
    answer = (answer + (S * x) % 1000000007) % 1000000007
print(answer)

"""
결국 구하고 싶은 것 -> (S * N^-1) % 1,000,000,007
                    -> (S * N^1,000,000,005) % 1,000,000,007 (by FLT)
결국 N^-1을 빨리 구하는 것이 관건이다.
이는 분할 정복을 이용한 거듭제곱 구하는 방법으로 해결하였다.
최종 answer는 10^9 + 7의 mod 값이 되어야 하는 것을 명심하자.
"""