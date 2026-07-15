def solution(s):
    answer = []
    last_seen = {}  
    
    for i, char in enumerate(s):
        if char not in last_seen:
            answer.append(-1)
        else:
            answer.append(i - last_seen[char])
        
        last_seen[char] = i
            
    return answer