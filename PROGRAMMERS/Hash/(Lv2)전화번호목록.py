def solution(phone_book):
    answer = True
    dic = {}
    # 일단 다 dict에 넣어놓음(dict key를 탐색하는 것은 O(1)로 충분하다.
    for pNumber in phone_book:
        dic[pNumber] = 1 
    # 각 원소에 대해
    for pNumber in phone_book: 
        temp = ""
        for num in pNumber: 
            temp += num
            # num의 접두어가 될 수 있는 temp가 dic에 있는지 체크함.
            if temp in dic and temp != pNumber:
                answer = False
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges