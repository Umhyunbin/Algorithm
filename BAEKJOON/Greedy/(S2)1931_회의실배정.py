import sys

N = int(input())
li = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
li.sort(key = lambda x : (x[1], x[0]))
cnt = 1
end = li[0][1]
for i in range(1, N):    
    if li[i][0] >= end:
        cnt += 1
        end = li[i][1]
print(cnt)