def solution(N, number):
    answer = -1
    dp = []
    # i -> N 개수
    for i in range (1, 9):     
        all_case = set()
        # {N}, {NN} , {NNN}...
        check_number = int(str(N) * i)
        all_case.add(check_number)
        
        # ex: N이 5개 필요한 경우 -> 0, 4(-1) / 1, 3(-1-1) / 2, 2(-2-1)...        
        for j in range(0, i - 1):
        # j 개를 사용해서 만든 값들        
            for op1 in dp[j]:
                for op2 in dp[-j-1] :
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)              
        if number in all_case:
            answer = i
            break
            
        dp.append(all_case) 
        
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges