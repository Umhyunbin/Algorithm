import sys
import re
input = sys.stdin.readline

p = re.compile("(100+1+|01)+")
T = int(input())
for i in range(T):
    radio = p.fullmatch(input().rstrip())
    if radio is None:
        print("NO")
    else:
        print("YES")