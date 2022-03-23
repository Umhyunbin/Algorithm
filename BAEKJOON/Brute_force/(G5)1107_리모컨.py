import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
broken = set(map(int, input().rstrip().split()))

answer = abs(100 - N)

for n in range(1000001):
    tmp = str(n)
    for i in range(len(tmp)):
        if int(tmp[i]) in broken:
            break
    else:
        answer = min(answer, len(tmp) + abs(n - N))
print(answer)

"""
500,000까지 있으므로 밑 -> 위, 위 -> 밑을 동시에 고려하기 위해
1,000,000까지 확인해야함.
하나씩 반복하면서 만들 수 없는 채널이면 넘어가거,
만들 수 있는 채널이면 기존 answer보다 작은지 비교하여 추가.
숫자 버튼(len(tmp)) + (+ , -)버튼(abs(n - N))이 총 누르는 수가 된다.
"""