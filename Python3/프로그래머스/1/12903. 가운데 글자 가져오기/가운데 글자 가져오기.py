def solution(s):
    c = 0
    c_2 = 0
    answer = []
    
    if len(s) % 2 == 1 :
        c = len(s) // 2 
        answer = s[c]
    else : 
        c_2 = len(s) // 2
        answer = s[c_2 -1 : c_2 + 1]
    return answer