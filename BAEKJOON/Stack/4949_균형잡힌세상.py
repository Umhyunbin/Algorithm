import sys

while True:
    s = []
    sen = sys.stdin.readline().rstrip()
    if sen == '.':
        break
    
    flag = True
    for i in sen:
        if i in ('(', '['):
            s.append(i)
        elif i in (')', ']'):
            if len(s) == 0:
                flag = False
                break
            elif (i == ')' and s[-1] == '(') or (i == ']' and s[-1] == '['):
                s.pop()
            else:
                flag = False
                break
    if len(s) != 0:
        flag = False
    if flag:
        print("yes")
    else:
        print("no")   
