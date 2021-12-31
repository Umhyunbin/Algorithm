import sys

N = int(sys.stdin.readline().rstrip())
s = list(range(1,N+1))
front, rear = -1, N-1

while front + 1 != rear:    
    s.append(s[front + 2])
    rear += 1
    front += 2
print(s[rear])

"""
front는 큐의 앞, rear는 큐의 뒤를 가리킴.
가장 위를 버리고, 그 다음 숫자를 가장 밑으로 바꾸어야 한다.

rear + 1을 통해 가장 위를 버리고, 
front + 2 번째를 s의 가장 아래에 새로 추가하여 2번째 위에 있던 숫자를
가장 밑으로 바꾸는 작업을 진행한다.

ex)
front ->
         1
         2
         3
rear ->  4

         1
front -> 2
         3
         4
rear ->  2

         1
         2
         3
front -> 4
         2
rear ->  4

         1
         2
         3
         4
         2
front -> 4
rear ->  4

따라서 답 : 4
"""
