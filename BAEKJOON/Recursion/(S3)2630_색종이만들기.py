import sys

N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().strip().split())))
idx = N
white, blue = 0, 0
s = [[0, 0]]
while len(s) > 0 and idx >= 1:   
    tmp = []
    l = len(s)
    for i in range(l):
        flag = True
        d = s.pop(0)
        x, y = d[0], d[1]        
        p = li[x][y]
        for j in range(x, x + idx):
            for k in range(y, y + idx):
                if li[j][k] != p:
                    flag = False
                    break
        if flag:
            if p == 0:
                white += 1
            else:
                blue += 1
        else:
            mid = idx // 2
            temp = [[x, y], [x, y + mid], [x + mid, y], [x + mid, y + mid]]
            for a in temp:
                tmp.append(a)
    s = tmp[:]   
    idx //= 2        
print(white)
print(blue)