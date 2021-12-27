import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    check = 0
    PS = sys.stdin.readline().rstrip()
    for c in PS:
        if c == '(':
            check += 1
        else:
            check -= 1
            if check < 0:
                break
    if check == 0:        
        print("YES")
    else:
        print("NO")


"""
() 짝이 맞아야함.
스택처럼 check 변수를 활용하여
( -> check += 1
) -> check -= 1

check이 무조건 0이어야 PS.(Parenthesis String)
중간에 check < 0 이라면 ( 보다 )가 많이 나온 상황
-> 무조건 NO
"""
