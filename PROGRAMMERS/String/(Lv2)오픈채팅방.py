def solution(record):
    """
    1. answer에 [아이디, 명령] 형태로 append
    2. Enter, Change -> 닉네임 변경 / Enter, Leave -> 메시지 출력
    3. Enter, Change에서 변경되는 닉네임의 마지막이 최종 출력 닉네임이 되어야하므로
       id를 key, nickname을 value로 하는 dict 설정.
    4. answer의 아이디를 id_nick의 값으로 변경하고 문자열 생성
    """
    answer = []
    id_nick = {}
    
    for r in record:
        elm = r.split()
        try:
            order, user_id, nickname = elm[0], elm[1], elm[2]
            if order == 'Enter':
                answer.append([user_id, "님이 들어왔습니다."])
                id_nick[user_id] = nickname            
            else:
                id_nick[user_id] = nickname
        except IndexError:
            order, user_id = elm[0], elm[1]
            answer.append([user_id, "님이 나갔습니다."])
    answer = list(map(lambda x: id_nick[x[0]] + x[1], answer))             
    
    return answer
