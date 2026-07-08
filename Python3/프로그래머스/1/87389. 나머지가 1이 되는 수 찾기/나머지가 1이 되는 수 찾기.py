def solution(n):
    answer = 0
    x = n    
    
    for i in range(1, x + 1):
        if n % i == 1:
            answer = i
            break;
    return answer