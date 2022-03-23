import sys
import heapq
           
N = int(sys.stdin.readline().rstrip())
hq = []
for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)
