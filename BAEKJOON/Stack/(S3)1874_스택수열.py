import sys

N = int(sys.stdin.readline().rstrip())
li, stk = [], []
cnt, flag = 1, 0

for i in range(N):
    num = int(sys.stdin.readline().rstrip())                
    while num >= cnt: 
        stk.append(cnt)
        cnt+=1
        li.append("+")        
    if stk[-1] == num:
        stk.pop()
        li.append("-")
    else:
        flag = -1
        break
    
if flag == -1:
    print("NO")
else:
    for i in li:
        print(i)
