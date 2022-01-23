import sys

N = int(input())
li = [0, 1, 1]

if N <= 3:
    print(li[N - 1])
else:
    for i in range(4, N + 1):
        temp = [li[-1]]
        if i % 3 == 0:
            temp.append(li[i // 3 - 1])
        if i % 2 == 0:
            temp.append(li[i // 2 - 1])
        li.append(min(temp) + 1)
    print(li[-1])

"""
X -> 1로 갈 수 있는 방법은 //3, //2, -1이 있다.
이를 할 수 있는 상황이면 temp에 추가시켜
가장 작은 것을 i값으로 설정.
"""
