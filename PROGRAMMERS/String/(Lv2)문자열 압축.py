from collections import deque

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) // 2 + 1):
        temp_len = len(s)
        # i개만큼 잘라서 deque 생성.
        li = deque(map(''.join, zip(*[iter(s)]*i)))

        while li:
            p = li.popleft()
            flag = 0
            # 중복되는만큼 추가 제거
            while li and li[0] == p:
                li.popleft()
                temp_len -= len(p)
                flag += 1
            if flag:
                # flag : 시작값이 얼마나 더 있는지 체크한 변수 -> 실제 개수는 flag + 1
                temp_len += len(str(flag + 1))
        # 새로 구한 값이 더 작으면 변경 
        answer = temp_len if temp_len < answer else answer
    
    return answer
