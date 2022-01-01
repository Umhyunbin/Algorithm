from collections import deque

def solution(bridge_length, weight, truck_weights):
    """
    done : 다리를 지난 트럭 수
    all_weight : 현재 다리 위에 있는 트럭의 무게 총합
    truck : 대기 트럭
    doing : 다리 위 트럭
    """
    answer, done, all_weight = 0, 0, 0
    fin = len(truck_weights)
    truck = deque(truck_weights)
    doing = deque()

    while done < fin:
        # 다리 위에 있는 트럭 1칸씩 이동
        for i in range(len(doing)):
            doing[i][1] -= 1

        # doing 맨 앞이 다리를 지날 수 있는 상태
        if doing and doing[0][1] == 0:
            f = doing.popleft()
            done += 1
            all_weight -= f[0]

        # 다리에 새로운 트럭이 올라올 수 있는 상황
        if truck and truck[0] + all_weight <= weight and len(doing) < bridge_length:
            doing.append([truck.popleft(), bridge_length])
            all_weight += doing[-1][0]

        answer += 1

    return answer

b = 2
w = 10
tw = [7, 4, 5, 6]

print(solution(b, w, tw))

"""
다리의 길이, 다리 최대 하중, 각 트럭의 무게가 주어진 상황에서
트럭이 다리를 모두 지날 수 있는 최소의 초 구하기(트럭 1칸-> 1초)
doing에 [트럭 무게, 남은 거리(다리 길이)] 를 넣은 뒤,
매 반복마다 각 doing의 남은 거리를 줄여주는 방식으로 계산.
출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenge
"""
