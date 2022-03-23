def judge(n1, n2, answer, k):
    for i in range(k):
        for j in range(k):
            if tree[n1+i][n2+j] != answer:
                return False
    return True

def quad(i1, i2, n):
    global s

    answer = tree[i1][i2]
    
    for i in range(i1, i1 + n):
        for j in range(i2, i2 + n):
            if answer != tree[i][j]:
                s += "("
                quad(i1, i2, n // 2)
                quad(i1, i2 + n // 2, n // 2)
                quad(i1 + n // 2, i2, n // 2)
                quad(i1 + n // 2, i2 + n // 2, n // 2)
                s += ")"
                return
    if answer == '0':
        s += '0'
    else:
        s += '1'
    
N = int(input())
s = ""
tree = []
for i in range(N):
    tree.append(input())

quad(0, 0, N)

print(s)