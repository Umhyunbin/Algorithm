import sys

input = sys.stdin.readline
N = int(input())
max_arr = list(map(int, input().rstrip().split()))
min_arr = [max_arr[i] for i in range(3)]
max_temp = [0] * 3
min_temp = [0] * 3
for i in range(1, N):
    x, y, z = map(int, input().rstrip().split())
    max_temp[0] = x + max(max_arr[0], max_arr[1])
    max_temp[1] = y + max(max_arr[0], max_arr[1], max_arr[2])
    max_temp[2] = z + max(max_arr[1], max_arr[2])

    min_temp[0] = x + min(min_arr[0], min_arr[1])
    min_temp[1] = y + min(min_arr[0], min_arr[1], min_arr[2])
    min_temp[2] = z + min(min_arr[1], min_arr[2])

    max_arr = [max_temp[i] for i in range(3)]
    min_arr = [min_temp[i] for i in range(3)]
print(max(max_arr), min(min_arr))

"""
메모리 제한이 걸려있으므로 이를 고려하여 1 * 3 짜리만 이용하자.

1 2 3
4 5 6
이라면

max
1 2 3
4 + max(1, 2) / 5 + max(1, 2, 3) / 6 + max(2, 3)
이런 식으로 반복함.
"""
