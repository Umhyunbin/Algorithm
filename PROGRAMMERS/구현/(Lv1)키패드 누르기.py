def Manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = ''    
    distance = [[i, j] for i in range(3) for j in range(3)]   
    distance = [[3, 1]] + distance  # 0 -> [3, 1]
    left, right = [3, 0], [3, 2]
    
    for n in numbers:
        if n % 3 == 1:
            answer += 'L'
            left = distance[n]
        elif n > 0 and n % 3 == 0:
            answer += 'R'
            right = distance[n]
        else:
            left2key = Manhattan_distance(distance[n], left)
            right2key = Manhattan_distance(distance[n], right)
            if left2key < right2key:
                answer += 'L'
                left = distance[n]
            elif left2key > right2key:
                answer += 'R'
                right = distance[n]
            elif hand == 'left':
                answer += 'L'
                left = distance[n]
            elif hand == 'right':
                answer += 'R'
                right = distance[n]  
    return answer
           
                
