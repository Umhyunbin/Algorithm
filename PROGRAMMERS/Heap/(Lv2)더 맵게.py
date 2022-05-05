import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        new_scoville = m1 + 2 * m2
        heapq.heappush(scoville, new_scoville)
        answer += 1
        if scoville[0] < K and len(scoville) == 1:
            answer = -1
            break
    return answer
