import sys

N = 123456 * 2 + 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False


def prime(v):
    cnt = 0
    for k in range(v + 1, v * 2 + 1):
        if sieve[k]:
            cnt += 1
    return cnt


li = []
while True:
    val = int(sys.stdin.readline().rstrip())
    if val == 0:
        break
    li.append(prime(val))
for a in li:
    print(a)