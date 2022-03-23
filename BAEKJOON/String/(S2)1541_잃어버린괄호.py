from collections import deque

exp = input()
number = deque(list(map(int, exp.replace("-", "+").split("+"))))
op = []
for i in range(len(exp)):
    if exp[i] == '+':
        if op and op[-1] == -1:
            op.append(-1)
        else:
            op.append(1)
    elif exp[i] == '-':
        op.append(-1)

result = number.popleft()

for i in range(len(op)):
    if op[i] == 1:
        result += number[i]
    else:
        result -= number[i]
print(result)

"""
괄호를 쳐야하는 상황은
++ / +- / -+ / -- 중 -+에만 해당됨.
ex) 55-50+40 -> 55-(50+40)해야 최소.
이는 분배법칙에 의해 55-50-40과 같다.

따라서 연산자를 추가할 때
연산자 리스트 맨 끝에 -가 있으면서 +를 추가해야 하는 상황이면
+ 대신 -를 추가하는 방식으로 문제 해결.

"""

"""
- 기준으로 일단 나누어놓고 각 원소 숫자들을 계산한 뒤,
처음은 더하고 나머지를 빼는 방식으로 생각할 수도 있다.

ex) 50 - 40 + 30 - 20 + 10
-> 50 - (40 + 30) - (20 + 10) 이 최소
-> '-'기준 split -> [50, 40+30, 20+10]
-> 각 원소들 계산해주고 맨 처음인 50은 덧셈, 나머지는 뺄셈으로 연산.
"""
