import sys
from collections import deque

itr = int(sys.stdin.readline())
for _ in range(itr):
    N, M = map(int, sys.stdin.readline().split())
    q = deque(list(map(int, sys.stdin.readline().split())))
    
    count = 0    
    while True:
        first = q[0]
        flag = True
        for i in range(1, len(q)):
            if first < q[i]:
                flag = False
                break
        if flag:             
            count += 1            
            if M == 0:  
                break
            else:
                q.popleft()
                M -= 1                
        else:            
            M = (M - 1) % len(q)
            q.append(q.popleft())
    print(count)

"""
남은 문서 중 현재 문서보다 중요도가 높은 문서가 하나라도 있으면 뒤에 재배치.

현재 문서(first)와 남은 문서를 비교하여
남은 문서의 중요도가 더 크면 flag = False

flag = True 면 현재 문서 중요도가 가장 크므로
count += 1을 한 뒤, 현재 문서가 관심 문서라면 break,
그렇지 않다면 popleft시키고 M은 1칸 앞으로 옴.

flag = False 면 앞으로 당김.
"""
