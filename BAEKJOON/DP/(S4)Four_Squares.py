n = int(input())

answer = [0] * (n + 1)

for i in range(1, n + 1):
    k = int(i ** 0.5)
    temp = n + 1
    for j in range(1, k + 1):
        temp = min(temp, answer[i - (j ** 2)])
    answer[i] = temp + 1
print(answer[n])

"""
i번째 기준으로 j ** 2(제곱수)만큼 차이나는 값들 중
가장 작은 값을 골라 + 1을 해준다.
ex) answer = [1, 2, 3, 1] 인 상태에서 answer[5]를 생각해보자.
2**2 < 5 < 3**2이므로 j 반복문은 1, 2를 확인하면 된다.

answer[5 - 1], answer[5 - 4]
-> 이렇게 i번째와 제곱수 차이나는 값들 중 가장 작은 값을 고르면,
거기서 뺀 제곱수만큼을 더해주는게 정답이 된다.
이 문제에서는 answer[5 - 1] = 1로 가장 작으므로(2**2이므로)
answer[5] = answer[4] + 1이 최소가 된다.
실제로 5 = 2**2 + 1**2 로 표현 가능하다.
"""
