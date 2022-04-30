def solution(absolutes, signs):
    answer = [absolutes[i] if signs[i] else -absolutes[i] 
              for i in range(len(absolutes))] 
    return sum(answer)
