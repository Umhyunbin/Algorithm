def make_matrix(row, column):
    """
    1 ~ row * column까지 matrix를 채움.
    """
    my_matrix = []
    i = 1
    for r in range(row):
        temp = []
        for c in range(column):
            temp.append(i)
            i += 1
        my_matrix.append(temp)
    return my_matrix

def solution(rows, columns, queries):
    """
    채워질 위치의 값을 temp로 빼놓고 넣을 값(start)을 자리에 넣어준 다음,
    start를 temp로 설정하여 반복할 수 있도록 함. 
    왼쪽 상단부터 시계방향으로 반복(index 조절)
    
    이 과정을 stack으로 구현한 풀이도 있음.
    temp를 stack에 push하고,
    stack[-2]를 start의 느낌으로 접근.
    """
    matrix = make_matrix(rows, columns)
    answer = []
    
    for q in queries:
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        start = matrix[x1][y1]
        rotate_list = []
        
        for i in range(y1 + 1, y2 + 1):
            rotate_list.append(start)
            temp = matrix[x1][i]
            matrix[x1][i] = start
            start = temp
            
        for i in range(x1 + 1, x2 + 1):
            rotate_list.append(start)
            temp = matrix[i][y2]
            matrix[i][y2] = start
            start = temp
            
        for i in range(y2 - 1, y1 - 1, -1):
            rotate_list.append(start)
            temp = matrix[x2][i]
            matrix[x2][i] = start
            start = temp
            
        for i in range(x2 - 1, x1 - 1, -1):
            rotate_list.append(start)
            temp = matrix[i][y1]
            matrix[i][y1] = start
            start = temp

        answer.append(min(rotate_list))
    return answer
                
