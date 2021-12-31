import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
stk = []
NGE = [-1] * N

for i in range(len(A)):
    while len(stk) != 0 and A[stk[-1]] < A[i]:
        NGE[stk.pop()] = A[i]
    stk.append(i)
   
for j in NGE:
    print(j, end=' ')


"""
반복문을 통해 현재 index 의 수가 다른 index의 오큰수가 될 수 있는지 판단.
ex) 3 5 2 7
i = 0
stk = [0]

i = 1
A[0] < A[1] -> NGE[0] = A[1]
stk = []
stk = [1]

만약 stk에 여러개의 index가 있었다면, stk에서 pop해서 쓰기 때문에
자신보다 오른쪽에 있으면서 더 큰 수 중 '가장 왼쪽'에 해당하는 값을 선택.
"""
