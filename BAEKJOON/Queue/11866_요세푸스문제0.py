li = list(map(int, input().split()))
N, K = li[0], li[1]
p = list(range(1, N + 1))
y = []

pivot = 0
for i in range(N):
    num = len(p)
    pivot = (pivot + K - 1) % num
    y.append(str(p.pop(pivot)))
print('<' + ', '.join(y) + '>')
