import sys

def check(x):
    for i in range(x):
        # 열이 같거나 대각선 상에 놓인 경
        if col[x] == col[i] or abs(col[i] - col[x]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            col[x] = i
            if check(x):
                dfs(x + 1)

input = sys.stdin.readline

N = int(input())

result = 0
col = [0] * 15  # 인덱스 번호 -> 행, 인덱스 값 -> 열
dfs(0)
print(result)