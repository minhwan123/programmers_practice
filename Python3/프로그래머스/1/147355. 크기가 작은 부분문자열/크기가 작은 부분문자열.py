def solution(t, p):
    answer = 0
    p_len = len(p)
    p_number = int(p)

    for i in range(len(t) - p_len + 1):
        number = int(t[i : i + p_len])
        
        if number <= p_number:
            answer += 1
            
    return answer