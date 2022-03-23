import sys
           
N, r, c = map(int, sys.stdin.readline().rstrip().split())
result = 0

while N > 0:   
    plus = 2 ** (2 * N - 2)  
    N -= 1
    if r < 2 ** N and c >= 2 ** N:
        result += plus
        c -= (2 ** N)
    elif r >= 2 ** N and c < 2 ** N:
        result += plus * 2
        r -= (2 ** N)
    elif r >= 2 ** N and c >= 2 ** N:
        result += plus * 3
        r -= (2 ** N)
        c -= (2 ** N)
print(result)