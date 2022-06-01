def make_list(s):
    """
    문자열에서 각 집합의 숫자를 추출하기 위한 함수.
    { 일때 시작해서 }가 되기 전까지 stack에 append하고,
    }가 되면 temp에 stack 자체를 저장.
    이를 ','로 구분한 다음 모든 원소를 정수로 만들고 집합에 씌워주면 최종 형태 완성.
    문제 해결을 위해 길이를 기준으로 정렬하여 return.
    """
    stack, temp, final = [], [], []
    
    for i in s[1: -1]:
        if i == '{':
            stack = []
        elif i == '}':
            temp.append("".join(stack))
        else:
            stack.append(i)
    final = [set(map(int, i.split(','))) for i in temp]
    
    return sorted(final, key = lambda x: len(x))

def solution(s):
    """
    현재 set_list는 길이순으로 정렬되어 있음.
    temp_set : 현재까지 answer에 들어간 원소들의 집합.
    set_list를 순회하면서 현재 집합 - temp_set이 새로 추가할 원소 !
    """
    answer, temp_set = [], set()
    set_list = make_list(s)
    
    for i in set_list:
        now = list(i - temp_set)[0]
        answer.append(now)
        temp_set.add(now)
    return answer

"""
1. 숫자를 전부 찾은 뒤, 각 숫자별 개수를 센다. (ex: '1' : 3, ...) (re.findall('\d+', s))
2. 이 dict를 value기준으로 내림차순 정렬(많이 나온 숫자가 먼저 오는 것이 맞음)한 다음,
   그때의 각 key들을 정수로 형변환하여 list 생성.
-> 이렇게 풀 수도 있다.
"""
