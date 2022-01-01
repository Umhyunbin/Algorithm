import sys
import heapq

def delete(h, v):
    while h and not v[h[0][1]]:
        heapq.heappop(h)

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    minhq, maxhq = [], []
    v = [False] * 1000001
    k = int(sys.stdin.readline().rstrip())
    for j in range(k):
        op, n = sys.stdin.readline().rstrip().split()
        if op == 'I':
            heapq.heappush(minhq, (int(n), j))
            heapq.heappush(maxhq, (-int(n), j))
            v[j] = True
        elif n == '1':            
            delete(maxhq, v)
            if maxhq:
                v[maxhq[0][1]] = False
                heapq.heappop(maxhq)
        else:
            delete(minhq, v)
            if minhq:
                v[minhq[0][1]] = False
                heapq.heappop(minhq)
    delete(maxhq, v)
    delete(minhq, v)
        
    if maxhq and minhq:
        print(-maxhq[0][0], minhq[0][0])
    else:
        print('EMPTY')


"""
maxhq [0] -> max 값. [1] -> max 값의 visited 확인 위한 idx
hq and not visited[hq[0][1]] -> hq의 원소는 아직 있는데
현재 루트 노드의 값이 visit처리 안되어 있다는 것은
다른 hq에서 이미 삭제 처리가 되었다는 뜻이므로 버리는게 맞음.

이렇게 삭제연산을 마친 다음 원소가 존재하면 그때 삭제처리.

"""
