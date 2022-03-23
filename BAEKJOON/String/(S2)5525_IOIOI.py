import sys
import re

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

result = 0
cnt = 0
idx = 1

while idx < M - 1:
    if S[idx - 1] == "I" and S[idx] == "O" and S[idx + 1] == "I":
        cnt += 1
        if cnt == N:
            cnt -= 1
            result += 1
        idx += 1
    else:
        cnt = 0
    idx += 1
print(result)
    